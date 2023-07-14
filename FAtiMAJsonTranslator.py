import random
import string
import time
import json
import re

from Constants.task_constants import ACTION_PLAN_TRANSLATION_TASK

occ_emotions_dict = {
    "admiration": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "[target]"
        }
    ],
    "anger": [
        {
            "Name": "Praiseworthiness",
            "Value": -5,
            "Target": "[target]"
        },
        {
            "Name": "Desirability",
            "Value": -5,
            "Target": "-"
        }
    ],
    "gratitude": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "[target]"
        },
        {
            "Name": "Desirability",
            "Value": 5,
            "Target": "-"
        }
    ],
    "distress": [
        {
            "Name": "Desirability",
            "Value": -5,
            "Target": "-"
        }
    ],
    "gratification": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "SELF"
        },
        {
            "Name": "Desirability",
            "Value": 5,
            "Target": "-"
        }
    ],
    "joy": [
        {
            "Name": "Desirability",
            "Value": 5,
            "Target": "-"
        }
    ],
    "pride": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "SELF"
        }
    ],
    "reproach": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "SELF"
        }
    ],
    "shame": [
        {
            "Name": "Praiseworthiness",
            "Value": 5,
            "Target": "SELF"
        }
    ],
    "happy-for": [],  # Does not have
    "hope": [
        {
            "Name": "Goal Success Probablity",
            "Value": 0.6,
            "Target": "GoodGoalName"
        }
    ],
    "relief": [
        {
            "Name": "Goal Success Probablity",
            "Value": 0,
            "Target": "BadGoalName"
        }
    ],
    "fears-confirmed": [],
    "fear": [
        {
            "Name": "Goal Success Probablity",
            "Value": 0.4,
            "Target": "BadGoalName"
        }],
    "gloating": [
        {
            "Name": "Desirability",
            "Value": 5,
            "Target": "-"
        },
        {
            "Name": "Desirability for others",
            "Value": -5,
            "Target": "[target]"
        }],
    "love": [
        {
            "Name": "Like",
            "Value": 5
        }],
    "hate": [
        {
            "Name": "Goal Success Probablity",
            "Value": -5
        }],
    "resentment": [
        {
            "Name": "Desirability",
            "Value": -5,
            "Target": "SELF"
        },
        {
            "Name": "Desirability for others",
            "Value": 5,
            "Target": "[target]"
        }],
    "satisfaction": [
        {
            "Name": "Goal Success Probablity",
            "Value": 1,
            "Target": "GoodGoalName"
        }],
    "disappointment": [
        {
            "Name": "Goal Success Probablity",
            "Value": 0,
            "Target": "GoodGoalName"
        }],
    "pity": [
        {
            "Name": "Desirability",
            "Value": -5,
            "Target": "-"
        },
        {
            "Name": "Desirability for others",
            "Value": -5,
            "Target": "[target]"
        }]
}


def remove_unwanted_caracters(argument):
    argument.strip()
    argument = re.sub("\.|\?|\!|\'", "", argument)
    argument = re.sub(r'\bSelf\b', "SELF", argument)
    argument = re.sub(r'\bproperty\b', "Property", argument)
    #arguments = argument.split(",")

    #for i, argument in enumerate(arguments):
        #argument = argument.strip()
    """argument = re.sub("[ ]+", " ", argument)
    argument = re.sub("\([ ]", "(", argument)
    argument = re.sub("[ ]\)", ")", argument)
    argument = re.sub("\)[ ]", ")", argument)
    argument = re.sub("\([ ]", "(", argument)"""
    argument = re.sub("[ ]+", " ", argument)
    argument = re.sub("^(\()\[", "([", argument)
    argument = re.sub("\]^(\))", "])", argument)


    argument = re.sub('_+', '_', argument)
    argument = re.sub('"', '', argument)
    argument = re.sub("[\{\}\:\/\\#\'\%\&\?«»\*\+\^;]", '', argument)
    argument = re.sub(r'(?<=[0-9a-zA-Z\_\-])\s+(?=[0-9a-zA-Z\_\-])', '_', argument)

    #arguments[i] = argument
    return argument
    #return ",".join(arguments)


def process_knowledge(knowledge, intentions):
    knowledge_base = {}
    for bel_des in knowledge:
        bel_des = remove_unwanted_caracters(bel_des)
        bel_des = re.sub("\[.*?\]", "", bel_des)
        bel_des = bel_des.split("=")
        value = bel_des[1].strip()
        bel_des = bel_des[0].strip()
        knowledge_base[bel_des] = value + ", 1" #Don't know it's 1

    for intention in intentions.keys():
        intention = remove_unwanted_caracters(intention)
        intention = re.sub("\[.*?\]", "", intention)
        intention = intention.split("=")
        intention = intention[1].strip()
        intention = intention[0].strip()
        knowledge_base[intention] = value + ", 1"  # Don't know it's 1

    return knowledge_base


def translate_action_to_event(agent, action):
    action = remove_unwanted_caracters(action)
    action = re.sub("SELF", agent, action)
    event = f"Event(Action-End, {agent}, {action}, *)"
    return event


def translate_effects_to_values(agent, effects):
    values = []
    for effect in effects:
        effect = remove_unwanted_caracters(effect)
        effect = re.sub("<|>", "=", effect)
        effect = re.sub("=+", "=", effect)

        arguments = effect.split("=")
        if len(arguments) < 2:
            continue

        value_dict = {
            "PropertyName": arguments[0].strip(),
            "NewValue": arguments[1].strip(),
            "ObserverAgent": agent
        }

        values.append(value_dict)
    return values


def parse_conditions(conditions):
    final_conditions = []
    for condition in conditions:
        condition = remove_unwanted_caracters(condition)
        condition = re.sub("<|>", "=", condition)
        condition = re.sub("=+", "=", condition)
        arguments = condition.split("=")
        #print(arguments)
        if len(arguments) != 2:
            continue
        if re.search('[\(\)\.\,\?\[\] ]', arguments[1].strip()):
            continue
        if not re.search('\(.*\)', arguments[0]):
            continue
        final_conditions.append(condition)
    return final_conditions

def add_intentions(intentions, action, conditions):
    for intention in intentions.keys():
        if action in intentions[intention]["action_plan"]:
            conditions.append(intention)
            return conditions
    return conditions

def parse_action_conditions(intentions, action, conditions):
    conditions = add_intentions(intentions, action, conditions)
    conditions = parse_conditions(conditions)
    return conditions

def get_initial_mood(mood):
    if mood:
        mood = mood[0]
        mood_args = re.split('[=<>]+', mood)
        if len(mood_args) < 2:
            return 0
        else:
            try:
                return int(mood_args[1])
            except:
                return 0
    return 0


def write_scenario_file(gpt_scenario):
    with open("FAtiMA_files/empty_scenario_fatima.json") as f:
        empty_scenario_json = json.load(f)

    empty_scenario_json["root"]["ScenarioName"] = gpt_scenario["scenario_name"]
    empty_scenario_json["root"]["Description"] = gpt_scenario["scenario_description"]

    for agent in gpt_scenario["agents"].keys():
        # Add characters/ agents
        character = {
            "KnowledgeBase": {
                "Perspective": agent,
                "Knowledge":
                    {
                        "SELF": process_knowledge(gpt_scenario["agents"][agent]["knowledge_base"], gpt_scenario["agents"][agent]["intentions"])
                    }
            },
            "BodyName": None,
            "VoiceName": None,
            "EmotionalState":
                {
                    "Mood": 0,
                    "initialTick": 0,
                    "EmotionalPool": [],
                    "AppraisalConfiguration":
                        {
                            "HalfLifeDecayConstant": 0.5,
                            "EmotionInfluenceOnMoodFactor": 0.3,
                            "MoodInfluenceOnEmotionFactor": 0.3,
                            "MinimumMoodValueForInfluencingEmotions": 0.5,
                            "EmotionalHalfLifeDecayTime": 15,
                            "MoodHalfLifeDecayTime": 60
                        }
                },
            "AutobiographicMemory":
                {
                    "Tick": 0,
                    "records": []
                },
            "OtherAgents":
                {
                    "dictionary": []
                },
            "Goals": []
        }

        empty_scenario_json["root"]["Characters"].append(character)

        for action in gpt_scenario["agents"][agent]["actions"].keys():
            event = translate_action_to_event(agent, action)
            values = translate_effects_to_values(agent, gpt_scenario["agents"][agent]["actions"][action]["effects"])

            empty_scenario_json["root"]["WorldModel"]["Effects"]["dictionary"].append({"key": event, "value": values})
            empty_scenario_json["root"]["WorldModel"]["Priorities"]["dictionary"].append({"key": event, "value": 1})

        for action in gpt_scenario["agents"][agent]["speak_actions"].keys():
            event = translate_action_to_event(agent, action)
            values = translate_effects_to_values(agent,
                                                 gpt_scenario["agents"][agent]["speak_actions"][action]["effects"])

            empty_scenario_json["root"]["WorldModel"]["Effects"]["dictionary"].append({"key": event, "value": values})
            empty_scenario_json["root"]["WorldModel"]["Priorities"]["dictionary"].append({"key": event, "value": 1})

    empty_scenario_json["root"]["Dialogues"] = []
    for dialogue in gpt_scenario["dialogue_tree"]:
        dialogue = re.sub("<|>", "", dialogue)
        dialogue_arguments = dialogue.split(",")
        if len(dialogue_arguments) < 5:
            continue
        current_state = remove_unwanted_caracters(dialogue_arguments[0])
        next_state = remove_unwanted_caracters(dialogue_arguments[1])
        meaning_state = remove_unwanted_caracters(dialogue_arguments[2])
        style_state = remove_unwanted_caracters(dialogue_arguments[3])
        utterance = dialogue_arguments[4]

        empty_scenario_json["root"]["Dialogues"].append(
            {
                "CurrentState": current_state,
                "NextState": next_state,
                "Meaning": meaning_state,
                "Style": style_state,
                "Utterance": utterance,
                "UtteranceId": generate_utterance_id()
            }
        )

    final_scenario_json = json.dumps(empty_scenario_json, indent=2)
    with open(f'{file_name.replace(".json", "")}_scenario_fatima.json', "w") as outfile:
        outfile.write(final_scenario_json)


def write_cognirules_file(gpt_scenario):
    # Rules json file ##################################################################################################
    ## Load empty rules file
    with open("FAtiMA_files/empty_rules_fatima.json") as f:
        empty_rules_json = json.load(f)

    ## Fill "EmotionalDecisionMakingAsset"
    for agent in gpt_scenario["agents"].keys():
        for action in gpt_scenario["agents"][agent]["actions"].keys():
            target = "-"
            action_arguments = action.split(',')
            if len(action_arguments) > 1:
                if action_arguments[1].strip() in gpt_scenario["agents"].keys():
                    target = action_arguments[1].strip()

            action_tendencies = {
                "Action": re.sub("SELF", agent, remove_unwanted_caracters(action)), #remove self from actions
                "Target": target,
                "Layer": "-",
                "Conditions": {
                    "Set": parse_action_conditions(gpt_scenario["agents"][agent]["intentions"], action, gpt_scenario["agents"][agent]["actions"][action]["conditions"])
                },
                "Priority": 1
            }

            empty_rules_json[1]["root"]["ActionTendencies"].append(action_tendencies)

            ## Fill "EmotionalAppraisalAsset"
            # faltam valores do manel (tirei eu do fatima - confirmar depois)
            occ_emotion = gpt_scenario["agents"][agent]["actions"][action]["occ_emotion"][0].lower() if \
                gpt_scenario["agents"][agent]["actions"][action]["occ_emotion"] else None
            try:
                appraisal_variables = occ_emotions_dict[occ_emotion]
            except:
                continue
            else:
                empty_rules_json[3]["root"]["AppraisalRules"]["Rules"] += [
                    {
                        "EventName": translate_action_to_event(agent, action),
                        "Conditions":
                            {
                                "Set": []
                            },
                        "AppraisalVariables": {"AppraisalVariables": appraisal_variables}
                    }
                ]

        for action in gpt_scenario["agents"][agent]["speak_actions"].keys():
            action_arguments = action.split(',')
            if len(action_arguments) < 4:
                continue

            conditions = parse_conditions(gpt_scenario["agents"][agent]["speak_actions"][action]["conditions"])
            if conditions:
                conditions = ["Has(Floor) = SELF", "DialogueState([target]) = [currentState]",
                              "IsAgent([target]) = True",
                              "ValidDialogue([currentState], [nextState], [meaning], [style]) = True"] + conditions
            else:
                conditions = ["Has(Floor) = SELF", "DialogueState([target]) = [currentState]",
                              "IsAgent([target]) = True",
                              "ValidDialogue([currentState], [nextState], [meaning], [style]) = True"]

            action_tendencies = {
                "Action": re.sub("SELF", agent, remove_unwanted_caracters(action)),
                "Target": '[target]',
                "Layer": "-",
                "Conditions": {
                    "Set": conditions

                },
                "Priority": 1
            }

            empty_rules_json[1]["root"]["ActionTendencies"].append(action_tendencies)

            ## Fill "EmotionalAppraisalAsset"
            # faltam valores do manel (tirei eu do fatima - confirmar depois)
            occ_emotion = gpt_scenario["agents"][agent]["speak_actions"][action]["occ_emotion"][0].lower() if \
                gpt_scenario["agents"][agent]["speak_actions"][action]["occ_emotion"] else None
            try:
                appraisal_variables = occ_emotions_dict[occ_emotion]
            except:
                continue
            else:
                empty_rules_json[3]["root"]["AppraisalRules"]["Rules"] += [
                    {
                        "EventName": translate_action_to_event(agent, action),
                        "Conditions":
                            {
                                "Set": []
                            },
                        "AppraisalVariables": {"AppraisalVariables": appraisal_variables}
                    }
                ]

    final_rules_json = json.dumps(empty_rules_json, indent=2)
    with open(f'{file_name.replace(".json", "")}_cognirules_fatima.json', "w") as outfile:
        outfile.write(final_rules_json)
    ####################################################################################################################


def generate_utterance_id():
    # sample_utterance_id = "TTS-0CC175B9C0F1B6A831C399E269772661"
    random_part = "175B9C0F1B6A831C399E269772661"

    # choose from all lowercase letter
    characters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(characters) for _ in range(len(random_part)))
    return "TTS-0CC" + result_str


if __name__ == "__main__":
    file_name = input("Write file name of gpt scenario file: ")

    # Load json with scenario info from chatgpt
    with open(file_name) as f:
        gpt_scenario = json.load(f)

    start_time = time.time()
    write_cognirules_file(gpt_scenario)

    # Scenario json file
    write_scenario_file(gpt_scenario)

    # print(type(empty_scenario_json))

    print("--- %s seconds ---" % ((time.time() - start_time)))
