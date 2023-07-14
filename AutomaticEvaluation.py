import json
import os


def load_scenarios(directory):
    scenarios_files = os.listdir(directory)
    scenarios = []

    for scenario_file in scenarios_files:
        with open(f'{directory}/{scenario_file}', 'r') as f:
            scenarios.append(json.load(f))

    return scenarios


def count_artifacts_scenario(scenario):
    # Count Agents
    try:
        agents = len(scenario["agents"].keys())
    except:
        return {
            "total": 0,
            "agents": 0,
            "beliefs": 0,
            "desires": 0,
            "intentions": 0,
            "actions": 0,
            "conditions": 0,
            "effects": 0,
            "emotion_before": 0,
            "emotion_after": 0,
            "dialogue_lines": 0,
            "speak_actions": 0,
            "speak_actions_conditions": 0,
            "speak_actions_effects": 0,
        }
    # Count beliefs and desires
    knowledge = 0
    beliefs = 0
    desires = 0
    for agent in (scenario["agents"].keys()):
        knowledge += len(scenario["agents"][agent]["knowledge_base"])

        for elem in scenario["agents"][agent]["knowledge_base"]:
            if "DES(" in elem:
                desires += 1
            elif "BEL(":
                beliefs += 1

    # Count intentions
    intentions = 0
    for agent in (scenario["agents"].keys()):
        intentions += len(scenario["agents"][agent]["intentions"])

    # Count actions
    actions = 0
    for agent in (scenario["agents"].keys()):
        try:
            actions += len(scenario["agents"][agent]["actions"].keys())
        except Exception as e:
            continue

    # Count Conditions
    # Count Effects
    conditions = 0
    effects = 0
    # Count emotions
    emotion_before = 0
    emotion_after = 0
    for agent in (scenario["agents"].keys()):
        try:
            for action in scenario["agents"][agent]["actions"].keys():
                conditions += len(scenario["agents"][agent]["actions"][action]["conditions"])
                effects += len(scenario["agents"][agent]["actions"][action]["effects"])
                emotion_before += len(scenario["agents"][agent]["actions"][action]["emotion_condition"])
                emotion_after += len(scenario["agents"][agent]["actions"][action]["occ_emotion"])
        except Exception as e:
            continue

    # Count speak actions
    speak_actions = 0
    for agent in (scenario["agents"].keys()):
        try:
            speak_actions += len(scenario["agents"][agent]["speak_actions"].keys())
        except Exception as e:
            continue

    # Count speak action conditions
    # Count speak action effects
    speak_actions_conditions = 0
    speak_actions_effects = 0
    for agent in (scenario["agents"].keys()):
        try:
            for sp in scenario["agents"][agent]["speak_actions"].keys():
                try:
                    speak_actions_conditions += len(scenario["agents"][agent]["speak_actions"][sp]["conditions"])
                    speak_actions_effects += len(scenario["agents"][agent]["speak_actions"][sp]["effects"])
                except:
                    continue
        except:
            continue

    # Count dialogue lines
    try:
        dialogue_lines = len(scenario["dialogue_tree"])
    except:
        dialogue_lines = 0

    total_scenario_artifacts = agents + knowledge + intentions + actions + conditions + effects + emotion_before + \
                               emotion_after + speak_actions + speak_actions_conditions + speak_actions_effects + \
                               dialogue_lines

    result = {
        "total": total_scenario_artifacts,
        "agents": agents,
        "beliefs": beliefs,
        "desires": desires,
        "intentions": intentions,
        "actions": actions,
        "conditions": conditions,
        "effects": effects,
        "emotion_before": emotion_before,
        "emotion_after": emotion_after,
        "dialogue_lines": dialogue_lines,
        "speak_actions": speak_actions,
        "speak_actions_conditions": speak_actions_conditions,
        "speak_actions_effects": speak_actions_effects,
    }

    return result


def count_artifacts_scenarios(scenarios):
    scenarios_counts = {
        "absolute": {
            "total": 0,
            "agents": 0,
            "beliefs": 0,
            "desires": 0,
            "intentions": 0,
            "actions": 0,
            "conditions": 0,
            "effects": 0,
            "emotion_before": 0,
            "emotion_after": 0,
            "dialogue_lines": 0,
            "speak_actions": 0,
            "speak_actions_conditions": 0,
            "speak_actions_effects": 0,
        },
        "mean": {
            "total": 0,
            "agents": 0,
            "beliefs": 0,
            "desires": 0,
            "intentions": 0,
            "actions": 0,
            "conditions": 0,
            "effects": 0,
            "emotion_before": 0,
            "emotion_after": 0,
            "dialogue_lines": 0,
            "speak_actions": 0,
            "speak_actions_conditions": 0,
            "speak_actions_effects": 0,
        }
    }

    for scenario in scenarios:
        scenario_count = count_artifacts_scenario(scenario)

        for type in scenarios_counts.keys():
            for key in scenarios_counts[type].keys():
                if type == "absolute":
                    scenarios_counts[type][key] += scenario_count[key]

                else:
                    scenarios_counts[type][key] += scenario_count[key] / len(scenarios)

    scenarios_counts["number_of_scenarios"] = len(scenarios)

    return scenarios_counts


def count_initial_actions_available(scenarios):
    available_initial_actions = 0
    conditions_in_knowledge_base = 0
    for scenario in scenarios:
        try:
            for agent in scenario["agents"].keys():
                try:
                    knowledge = scenario["agents"][agent]["knowledge_base"]
                    for action in scenario["agents"][agent]["actions"].keys():
                        try:
                            conditions = scenario["agents"][agent]["actions"][action]["conditions"]
                            if all(item in knowledge for item in conditions):
                                available_initial_actions += 1
                            else:
                                conditions_in_knowledge_base += len([v for v in conditions if v in knowledge])
                        except:
                            continue
                except:
                    continue
        except:
            continue

    return available_initial_actions, conditions_in_knowledge_base


def action_available(agent, action, knowledge, scenario):
    return all(item in knowledge for item in scenario["agents"][agent]["actions"][action]["conditions"])


def apply_effects(agent, action, knowledge, scenario):
    effects = scenario["agents"][agent]["actions"][action]["effects"]

    effect_values = {e.split("=")[0]: e.split("=")[1] for e in effects}
    knowledge_values = {e.split("=")[0]: e.split("=")[1] for e in knowledge}

    for e in effect_values.keys():
        if e in knowledge_values.keys():
            knowledge_values[e] = effect_values[e]

    knowledge = ["=".join([k, knowledge[k]]) for k in knowledge_values.keys()]

    return knowledge


def count_action_sequences(scenarios):
    sequence_sizes = {}
    for scenario in scenarios:
        try:
            sequence_sizes[scenario["scenario_name"]] = {agent: [] for agent in scenario["agents"].keys()}
            try:
                for agent in scenario["agents"].keys():
                    try:
                        knowledge = scenario["agents"][agent]["knowledge_base"]
                        for intention in scenario["agents"][agent]["intentions"].keys():
                            sequence = []
                            sequence_sizes[scenario["scenario_name"]][agent].append(sequence)
                            try:
                                for action in scenario["agents"][agent]["intentions"][intention]["action_plan"]:
                                    try:
                                        conditions = scenario["agents"][agent]["actions"][action]["conditions"]
                                        if all(item in knowledge for item in conditions):
                                            sequence.append(action)
                                            sequence_sizes[scenario["scenario_name"]][agent][-1] = sequence
                                            knowledge = apply_effects(agent, action, knowledge, scenario)
                                    except:
                                        continue
                            except:
                                continue
                    except:
                        continue
            except:
                continue
        except:
            continue
    return len(sequence_sizes.keys()), sequence_sizes



def count_reachable_intentions(scenarios):
    sequence_sizes = {}
    intentions_completed = 0
    for scenario in scenarios:
        try:
            sequence_sizes[scenario["scenario_name"]] = {agent: [] for agent in scenario["agents"].keys()}
            try:
                for agent in scenario["agents"].keys():
                    try:
                        knowledge = scenario["agents"][agent]["knowledge_base"]
                        for intention in scenario["agents"][agent]["intentions"].keys():
                            sequence = []
                            sequence_sizes[scenario["scenario_name"]][agent].append(sequence)
                            try:
                                for action in scenario["agents"][agent]["intentions"][intention]["action_plan"]:
                                    try:
                                        conditions = scenario["agents"][agent]["actions"][action]["conditions"]
                                        if all(item in knowledge for item in conditions):
                                            sequence.append(action)
                                            sequence_sizes[scenario["scenario_name"]][agent][-1] = sequence
                                            knowledge = apply_effects(agent, action, knowledge, scenario)
                                    except:
                                        continue

                            except:
                                continue

                            if len(sequence) == len(
                                    scenario["agents"][agent]["intentions"][intention]["action_plan"]):
                                intentions_completed += 1
                    except:
                        continue
            except:
                continue
        except:
            continue

    return intentions_completed


if __name__ == "__main__":
    # load scenarios
    scenarios = load_scenarios("Data")

    # How much artifacts it creates
    # How much artifacts it creates
    ## How many agents
    ## How many beliefs
    ## How many desires
    ## How many intentions
    ## How many actions
    artifacts = count_artifacts_scenarios(scenarios)
    print(artifacts)

    # How many sequence of actions are feasable
    ## What is the size of the sequence
    ## How many conditions are wrong

    # How many actions are available to the agent right from the beginning
    # For the actions not available, how many conditions are in the knowledge base
    initial_actions_available, conditions_in_knowledge_base = count_initial_actions_available(scenarios)
    print(initial_actions_available, conditions_in_knowledge_base)

    # How long are the sequences of actions
    n_sequences, sequence_sizes = count_action_sequences(scenarios)
    print(n_sequences, sequence_sizes)

    intentions_completed = count_reachable_intentions(scenarios)
    print(intentions_completed)