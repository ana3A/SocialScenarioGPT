TASK_DESCRIPTION = """The task is to create a game scenario with socially intelligent agents that can perform actions 
with consequences based on their emotional state and follow the BDI architecture. The Belief-Desire-Intention model 
provides a framework for creating agents that can exhibit complex behavior, plan, and adapt to changing environments. 
The BDI model has three main components: Beliefs: Beliefs represent the informational state of the agent, 
in other words, its beliefs about the world (including itself and other agents). It can include properties of agents 
and objects and relationships with other agents or things. Desires: Desires represent the motivational state of the 
agent. They represent objectives or situations that the agent would like to accomplish or bring about. Examples of 
desires might be: "find the best price", "go to the party" or "become rich". Intentions: Intentions represent the 
deliberative state of the agent – what the agent has chosen to do. Intentions are desires to which the agent has to 
some extent committed. In implemented systems, this means the agent has begun executing a plan. In our case, 
Intentions will be represented as Actions agents can choose to perform, motivated by their beliefs and desires. """

SCENARIO_DESCRIPTION_GENERATIVE_TASK = """
The social scenario description is:

"[[DESCRIPTION HERE]]" 


"""

"""Use your knowledge and commonsense to create the most interesting game world you can think of, with agents that act 
in a believable manner, react emotionally, and have beliefs and desires which motivate their actions. Describe how 
each agent should respond with appropriate social practices and roles to different situations. """

AGENT_TRANSLATION_TASK = """
Write "The agents are:" and list the agents that can appear in the social scenario. 
Names of agents can only have letters, numbers and underscores. 
Write each name between double square brackets. Use underscores instead of spaces.
"""

BELIEFS_DESIRES_TRANSLATION_TASK = """Translate the beliefs and desires of the agent [[AGENT NAME]] into a symbolic 
representation. You can add more beliefs or desires using your common sense. 
Beliefs are translated as: [[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]]

and Desires are translated as: [[DES(CharacterWithGoal, Arguments*) = True/False/Numerical Value]]
 
Beliefs and Desires can have one or more arguments separated by commas, each argument can have letters, numbers or 
underscores and can not be strings. Each beliefs describes only one belief, and each desire describes only one desire.
Do not forget the double squared brackets at the beginning and end of each belief and desire and arguments can not be strings.
Use underscores instead of spaces.
"""

INTENTS_TRANSLATION_TASK = """
Based on the provided beliefs and deisres, list the intentions of the agent [[AGENT NAME]]
 into [[INTENT(CharacterWithIntent, Arguments*) = True/False/Numerical Value]], where the 
argument CharacterWithIntent is the character with the intent, and an intent can have more arguments separated by commas.

Intentions can have one or more arguments separated by commas, each argument can have letters, numbers or 
underscores and can not be strings. Each intent describes only one intention.
Do not forget the double squared brackets at the beginning and end of each intention and arguments can not be strings.
Use underscores instead of spaces.

List and translate the intentions of the agent [[AGENT NAME]] in the form [[INTENT(CharacterWithIntent, Arguments*) = True/False/Numerical Value]]. 
Only list the INTENTIONS in the form [[INTENT(CharacterWithIntent, Arguments*) = True/False/Numerical Value]].
"""

ACTION_PLAN_TRANSLATION_TASK = """Based on the intention [[INTENTION]] plan a sequence of actions in chronological 
order that the agent [[AGENT]] can do to achieve it's intention. Actions follow the format [[ActionName(AgentOfAction, TargetOfAction, Arguments*)]] where ActionName is the name of 
the action, AgentOfAction is who performs the action, TargetOfAction is who or what is the target of the action, 
and then each action can have more arguments or not. """

INITIAL_MOOD_TASK = """
What is the initial mood of the agent [[AGENT NAME]] at the beginning of the scenario?
Translate the initial mood into a value between -10 and 10, were -10 is the worst possible mood and 10 is the best possible mood.
Translate the mood to this format:
[[Mood(SELF)=x]], where x is a value between -10 and 10
 """

INITIAL_EMO_TASK = """
Emotions in FAtiMA are based on the OCC theory of emotions. Emotions represent valenced (
good or bad) reactions to events/perceptions of the world 

OCC defines a set of emotions:
Joy: 	(pleased about) a desirable event
Distress: 	(displeased about) an undesirable event
Happy-for: 	 (pleased about) an event presumed to be desirable for someone else
Pity: 	(displeased about) an event presumed to be undesirable for someone else
Gloating: 	(pleased about) an event presumed to be undesirable for someone else
Resentment: 	(displeased about) an event presumed to be desirable for someone else
Hope: 	 (pleased about) the prospect of a desirable event
Fear: 	(displeased about) the prospect of an undesirable event
Satisfaction: 	 (pleased about) the confirmation of the prospect of a desirable event
Fears-confirmed: 	(displeased about) the confirmation of the prospect of an undesirable event
Relief: 	(pleased about) the disconfirmation of the prospect of an undesirable event
Disappointment: 	 (displeased about) the disconfirmation of the prospect of a desirable event
Pride: 	(approving of) one’s own praiseworthy action
Shame: 	(disapproving of) one’s own blameworthy action
Admiration: 	(approving of) someone else’s praiseworthy action
Reproach: 	 (disapproving of) someone else’s blameworthy action
Gratification: 	 (approving of) one’s own praiseworthy action and (being pleased about) the related desirable event
Remorse: 	(disapproving of) one’s own blameworthy action and (being displeased
Gratitude: 	(approving of) someone else’s praiseworthy action and (being pleased about) the related desirable event
Anger: 	(disapproving of) someone else’s blameworthy action and
(being displeased about) the related undesirable event
Love: 	(liking) an appealing object
Hate: 	(disliking) an unappealing object

Decide which the agent [[AGENT NAME]] feels at the beginning of the scenario. Write one of the emotions 
from OCC model between double brackets. 
Do not forget the double squared brackets.
"""

ACTION_TRANSLATION_TASK = """
Translate the intents into actions in a symbolic representation.

Actions follow the format [[ActionName(AgentOfAction, TargetOfAction, Arguments*)]] where ActionName is the name of 
the action, AgentOfAction is who performs the action, TargetOfAction is who or what is the target of the action, 
and then each action can have more arguments or not. 

Translate each action of the agent [[AGENT NAME]] into the form [[ActionName(AgentOfAction, TargetOfAction, 
Arguments*)]]. You can add more actions using your common sense. 
Do not forget the double squared brackets and arguments can not be strings. Use underscores instead of spaces."""

CONDITIONS_EFFECTS_TASK = """Intents or actions are motivated by an agent's beliefs and desires, meaning there are 
conditions that need to be meet to perform an action. Conditions should contain beliefs and desires already defined. 
Actions have effects after agent's perform them. The effects can change the beliefs and desires of agent's or create 
new ones. 

Translate the effects and conditions of the action [[ACTION]] performed by the agent [[AGENT NAME]].

Write "Conditions:" before listing the conditions and write "Effects:" before listing the effects.
Beliefs are represented as: [[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]]
Desires are represented as: [[DES(CharacterWithGoal, Arguments*) = True/False/Numerical Value]]
The arguments can only have letters, numbers and underscores or be variables between square brackets.
Do not forget the double squared brackets and arguments can not be strings. Use underscores instead of spaces.
"""

CONDITIONS_EFFECTS_TASK_int = """Actions are motivated by an agent's beliefs and desires, meaning there are 
conditions that need to be meet to perform an action. Conditions should contain the intention and the beliefs and desires that lead to the action. 
Actions have effects after agent's perform them. The effects can change the intentions, beliefs and desires of agent's or create 
new ones. 

Translate the effects and conditions of the action [[ACTION]] performed by the agent [[AGENT NAME]].

Write "Conditions:" before listing the conditions and write "Effects:" before listing the effects.
Beliefs are represented as: [[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]]
Desires are represented as: [[DES(CharacterWithGoal, Arguments*) = True/False/Numerical Value]]
Intentions are represented as: [[INTENT(CharacterWithIntention, Arguments*) = True/False/Numerical Value]]
The arguments can only have letters, numbers and underscores or be variables between square brackets.
Do not forget the double squared brackets and arguments can not be strings. Use underscores instead of spaces.
"""

DIALOGUE_TREE_TASK = """
Define dialogues that can be had by the characters. Define the dialogues in dialogue turns and write them in the form:
[[CurrentState, NextState, Meaning, Style, UtteranceText]]

The Current State defines the state of the conversation, the Next State defines where the conversation will move to 
next, the Meaning and Style fields are used for auxiliary tags, typically we use them to define if a dialogue has a 
particular personality trait or discusses a particular context but it can be used as a flag for anything the author 
wants. 

Generate the dialogue turns in the format [[CurrentState, NextState, Meaning, Style, UtteranceText]]. Write the 
UtteranceText between quotation marks. Define the Meaning and Style as well. CurrentState, NextState, Meaning and Style can only have letters and numbers. 
"""

EVENTS_TRANSLATION_TASK = """
Translate the action  [ACTION] performed by [AGENT NAME] into one and only one of three representations:

Action-Start:  [[Event(Action-Start, AgentOfAction, ActionName, TargetOfAction)]]
Action-End: [[Event(Action-End, AgentOfAction, ActionName, TargetOfAction)]]
Property-Change: [[Event(Property-Change, AgentOfAction, Property Name, New Value)]]

Remember that actions were defined as [ActionName(AgentOfAction, TargetOfAction, Arguments*)]] where ActionName is 
the name of the action, AgentOfAction is who performs the action, TargetOfAction is who or what is the target of the 
action. 
"""

SPEAK_ACTION_TASK = """
List each dialogue turn that the agent [[AGENT NAME]] can say in the form 
[[CurrentState, NextState, Meaning, Style, UtteranceText]]
 """

SPEAK_CONDITIONS_EFFECTS = """
Speak actions' conditions are the beliefs, desires and intents an agent needs to have in order to perform the action. 
The speak actions' effects are the new beliefs and/or goals the agents now have after performing the action. Old beliefs or goals can also be changed after performing the action.

Translate the effects and conditions of the speak action [[SPEAK ACTION]] performed by the agent [[AGENT NAME]] into the language representation. 
Write "Conditions:" before listing the conditions and write "Effects" before listing the effects. Put each belief, desire and intention between double brackets as in:
[[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]]
[[DES(CharacterWithDesire, Arguments*) = True/False/Numerical Value]]
[[INTENT(CharacterWithGoal, Arguments*) = True/False/Numerical Value]]
The arguments can only have letters, numbers and underscores or be variables between square brackets.
"""

ACTIONS_EMO_APPRAISAL = """Emotions in FAtiMA are based on the OCC theory of emotions. Emotions represent valenced (
good or bad) reactions to events/perceptions of the world 

OCC defines a set of emotions:
Joy: 	(pleased about) a desirable event
Distress: 	(displeased about) an undesirable event
Happy-for: 	 (pleased about) an event presumed to be desirable for someone else
Pity: 	(displeased about) an event presumed to be undesirable for someone else
Gloating: 	(pleased about) an event presumed to be undesirable for someone else
Resentment: 	(displeased about) an event presumed to be desirable for someone else
Hope: 	 (pleased about) the prospect of a desirable event
Fear: 	(displeased about) the prospect of an undesirable event
Satisfaction: 	 (pleased about) the confirmation of the prospect of a desirable event
Fears-confirmed: 	(displeased about) the confirmation of the prospect of an undesirable event
Relief: 	(pleased about) the disconfirmation of the prospect of an undesirable event
Disappointment: 	 (displeased about) the disconfirmation of the prospect of a desirable event
Pride: 	(approving of) one’s own praiseworthy action
Shame: 	(disapproving of) one’s own blameworthy action
Admiration: 	(approving of) someone else’s praiseworthy action
Reproach: 	 (disapproving of) someone else’s blameworthy action
Gratification: 	 (approving of) one’s own praiseworthy action and (being pleased about) the related desirable event
Remorse: 	(disapproving of) one’s own blameworthy action and (being displeased
Gratitude: 	(approving of) someone else’s praiseworthy action and (being pleased about) the related desirable event
Anger: 	(disapproving of) someone else’s blameworthy action and
(being displeased about) the related undesirable event
Love: 	(liking) an appealing object
Hate: 	(disliking) an unappealing object

Decide which the agent [[AGENT NAME]] feels after performing the action [[ACTION]]. Write one of the emotions 
from OCC model between double brackets. 
Do not forget the double squared brackets.
"""

EMOTION_CONDITION_TASK = """
Emotions in FAtiMA are based on the OCC theory of emotions. Emotions represent valenced (
good or bad) reactions to events/perceptions of the world 

OCC defines a set of emotions:
Joy: 	(pleased about) a desirable event
Distress: 	(displeased about) an undesirable event
Happy-for: 	 (pleased about) an event presumed to be desirable for someone else
Pity: 	(displeased about) an event presumed to be undesirable for someone else
Gloating: 	(pleased about) an event presumed to be undesirable for someone else
Resentment: 	(displeased about) an event presumed to be desirable for someone else
Hope: 	 (pleased about) the prospect of a desirable event
Fear: 	(displeased about) the prospect of an undesirable event
Satisfaction: 	 (pleased about) the confirmation of the prospect of a desirable event
Fears-confirmed: 	(displeased about) the confirmation of the prospect of an undesirable event
Relief: 	(pleased about) the disconfirmation of the prospect of an undesirable event
Disappointment: 	 (displeased about) the disconfirmation of the prospect of a desirable event
Pride: 	(approving of) one’s own praiseworthy action
Shame: 	(disapproving of) one’s own blameworthy action
Admiration: 	(approving of) someone else’s praiseworthy action
Reproach: 	 (disapproving of) someone else’s blameworthy action
Gratification: 	 (approving of) one’s own praiseworthy action and (being pleased about) the related desirable event
Remorse: 	(disapproving of) one’s own blameworthy action and (being displeased
Gratitude: 	(approving of) someone else’s praiseworthy action and (being pleased about) the related desirable event
Anger: 	(disapproving of) someone else’s blameworthy action and
(being displeased about) the related undesirable event
Love: 	(liking) an appealing object
Hate: 	(disliking) an unappealing object

Decide which the agent [[AGENT NAME]] feels before performing the action [[ACTION]]. Write one of the emotions 
from OCC model between double brackets. 
Do not forget the double squared brackets.
"""

SPEAK_ACTIONS_EMO_APPRAISAL = """The OCC model of emotions suggests that emotions result from appraisals of events, 
which evaluate their significance for an individual's goals and well-being. Emotions in FAtiMA are based on the OCC 
theory of emotions. Emotions represent valenced ( good or bad) reactions to events/perceptions of the world 

OCC defines a set of emotions:
Joy: 	(pleased about) a desirable event
Distress: 	(displeased about) an undesirable event
Happy-for: 	 (pleased about) an event presumed to be desirable for someone else
Pity: 	(displeased about) an event presumed to be undesirable for someone else
Gloating: 	(pleased about) an event presumed to be undesirable for someone else
Resentment: 	(displeased about) an event presumed to be desirable for someone else
Hope: 	 (pleased about) the prospect of a desirable event
Fear: 	(displeased about) the prospect of an undesirable event
Satisfaction: 	 (pleased about) the confirmation of the prospect of a desirable event
Fears-confirmed: 	(displeased about) the confirmation of the prospect of an undesirable event
Relief: 	(pleased about) the disconfirmation of the prospect of an undesirable event
Disappointment: 	 (displeased about) the disconfirmation of the prospect of a desirable event
Pride: 	(approving of) one’s own praiseworthy action
Shame: 	(disapproving of) one’s own blameworthy action
Admiration: 	(approving of) someone else’s praiseworthy action
Reproach: 	 (disapproving of) someone else’s blameworthy action
Gratification: 	 (approving of) one’s own praiseworthy action and (being pleased about) the related desirable event
Remorse: 	(disapproving of) one’s own blameworthy action and (being displeased
Gratitude: 	(approving of) someone else’s praiseworthy action and (being pleased about) the related desirable event
Anger: 	(disapproving of) someone else’s blameworthy action and
(being displeased about) the related undesirable event
Love: 	(liking) an appealing object
Hate: 	(disliking) an unappealing object

Decide which the agent [[AGENT NAME]] feels after performing the action [[SPEAK ACTION]]. Write one of the emotions 
from OCC model between double brackets. 
Do not forget the double squared brackets.
"""

ACTION_MOOD = """
FAtiMA Toolkit has a variable called Mood that goes from -10 to 10. -10 is the worst mood possible while 10 is the best. 
Agents with Mood above 0 have a positive mood and below 0 have a negative mood. If it's 0 it's neutral.

Define the mood the agent [[AGENT NAME]] has to have to perform the action [[ACTION]].
Write the mood as [[Mood(SELF) < x]], [[Mood(SELF) > x]] or [[Mood(SELF) = x]], where x is an integer value.
Do not forget the double squared brackets.
"""

SPEAK_ACTION_MOOD = """
FAtiMA Toolkit has a variable called Mood that goes from -10 to 10. -10 is the worst mood possible while 10 is the best. 
Agents with Mood above 0 have a positive mood and below 0 have a negative mood. If it's 0 it's neutral.

The mood is defined as:

Mood(SELF) < x, Mood(SELF)>x or Mood(SELF)=x, where x is an integer value.

Define the mood the agent [[AGENT NAME]] has to have to perform the speak action [[SPEAK ACTION NAME]].
Write the mood as [[Mood(SELF) < x]], [[Mood(SELF) > x]] or [[Mood(SELF) = x]].
"""


######################################################################################################################

CONDITIONS_EFFECTS_TASKold = """
For each agent, list the actions they can make along with each action's conditions and effects. 
Actions' conditions are the beliefs and intents/goals an agent needs to have in order to perform the action. 
The actions' effects are the new beliefs and/or goals the agents now have after performing the action. Old beliefs or goals can also be changed after performing the action.

Beliefs and goals are composed of names and conditions, meaning they can be true or false. When a goal is being pursued or a belief is true it has to be equal to true. When a goal is no longer active or a belief is no longer true for the agent, is has to be equal to false. Actions may change the goals and beliefs from true to false and vice-versa. Actions might also require or create new goals and beliefs. 

Define beliefs as [[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]] and goals as [[INTENT(CharacterWithGoal, Arguments*) = True/False/Numerical Value]].
Remember that actions were defined as [[ActionName(AgentOfAction, TargetOfAction, Arguments*)]].

If a belief or an goal is part of the conditions of an action, generate beliefs as COND[[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]] and a goal as COND[[INTENT(CharacterWithGoal, Arguments*) = True/False/Numerical Value]].
Of a belief or goal is aprt of the effects of an action, generate beliefs as goals as EFFECT[[BEL(CharacterWithBelief, Arguments*) = True/False/Numerical Value]] and EFFECT[[INTENT(CharacterWithGoal, Arguments*) = True/False/Numerical Value]]

For each agent, list the conditions, the action, and then the effects like this:

"AgentName:" Name of the agent here
"Conditions:" list the conditions of action here
"Action:" put the action here
"Effects:" list the effects of action here
"""

ACTION_TRANSLATION_TASKold = """
I want to translate all this information about the first scene into a symbolic representation that I can then use as a programming language. The symbolic representation is inspired and similar to first-order logic.

The symbolic representation follows these rules:
Symbols: Represent constant entities (actions, objects, name of properties, name of relations) Ex: “Sam”, “A1”, “Table” 
Variables: Represent an entity or value that is not specified yet Can be replaced by symbols Ex: “[x]”, “[target]” 
Composed Names Represent properties or relations Ex: “Likes(Emys,Chocolate)”, “Has(Sam, [x])”.

Actions usually follow the format [[ActionName(AgentOfAction, TargetOfAction, Arguments*)]] where ActionName is the name of the action, usually a verb, the first argument AgentOfAction is who performs the action, the second argument TargetOfAction is who or what is the target of the action, and then each action can have more arguments or not.

Considering the goals, the beliefs and the actions previously described, list and translate each action into a correct symbolic representation. Each action must be written between brackets [] like this [].
"""

TASK_DESCRIPTION_OLD = """

I want to create a game scenario with socially intelligent agents/characters that, in certain circumstances, can perform actions that have consequences for them. I want to define a description of the social scene that describes the agents and the general interaction. You need to create the most interesting world that allows the agents to interact with each other and complete their goals.  I also want this to be a scenario with multiple possible interaction paths. Everything the agents do depends on their emotional state as well. I want a world with locations, each location to have a set of actions available for the characters to do, along with their requirements (because for an action to be available some conditions need to be met) and their consequences com the characters and the world. I want the characters/agents to follow the BDI architecture.

The Belief-Desire-Intention (BDI) software model is an architecture for designing intelligent agents that was inspired by human practical reasoning. The BDI model provides a robust framework for creating agents that can exhibit complex behavior, plan, and adapt to changing environments. It is based on three main components: 1. Beliefs: These represent an agent's knowledge or understanding of the world, including facts, assumptions, and uncertain information. Beliefs are often subject to change as an agent receives new information, allowing it to update its understanding of the world. 2. Desires: Desires represent an agent's goals or preferences. They are the motivations driving the agent's behavior and help determine which actions the agent should pursue. Desires can change over time as an agent gains new information or experiences, and they can also conflict with one another. 3. Intentions: Intentions are the specific plans or commitments an agent forms based on its desires and beliefs. These are the courses of action that the agent has chosen to pursue in order to achieve its goals. Intentions are generally more stable than desires, as they represent a commitment to a particular course of action. The BDI model allows for the creation of agents that can reason about their actions, dynamically adjust their goals and intentions, and interact with other agents in complex environments. This architecture has been widely used in various applications, including multi-agent systems, virtual characters in video games, and intelligent personal assistants.

Say "Read." after you read it.
"""

SCENARIO_DESCRIPTION_AGENT_TASKold = """
The social scenario descriptions is the following:

[[DESCRIPTION HERE]]

Use your knowledge and commonsense to list the agents that appear in the social scenario.
The names of the agents can only have letters, numbers and underscores. 
Write each name between square brackets. List a maximum of three characters.
"""

MULTIPLE_SCENE_TASK = """
Use your common sense to generate multiple scenes where the interaction between the agents is different. The agents should react based on the appropriate social norms. Make different scenes for when some agents have a positive mood and a negative mood for example, or when something important happens.

Generate a maximum of 3 scenes and enumerate the scenes as Scene 1, Scene 2 and Scene 3.
"""

MAXIMUM_SCENES = 3

SCENE_X_TASK = """
For the [[nth]] scene, use your common sense and describe possible beliefs and goals each agent can have and what actions each agent can perform in the [[nth]] scene.
Note that actions are motivated by the goals and beliefs.
"""