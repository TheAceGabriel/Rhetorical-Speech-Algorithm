import json

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def generate_speech(config):
    leader = config['leader']
    topic = config['topic']
    audience = config['audience']
    goal = config['goal']
    values = config['values']
    positive_vision = config['positive_vision']
    future_goal = config['future_goal']
    adversary = config['adversary']
    emotion = config['emotion']
    actions = config['actions']

    # Building the speech
    introduction = f"My fellow {audience}, today we stand at a crossroads."
    leader_statement = f"As your {leader}, I stand before you as a {topic} advocate."
    repeated_message = (f"How long can we allow {adversary} to hinder our {goal}? ") * 3
    rhetorical_question = "Are we ready to rise to the occasion?"
    core_values = f"We believe in the core values of {', '.join(values[:-1])}, and {values[-1]}."
    call_to_action = f"It is these values that will guide us as we {', '.join(actions[:-1])}, and {actions[-1]}."
    emotional_appeal = f"I feel the {emotion} in every corner of this nation!"
    vision_for_future = f"Let us strive for {positive_vision}. Together, we will {goal}, and through unity, achieve {future_goal}."
    closing = f"Together, we will {positive_vision}. Together, we will succeed! Thank you, and may {topic} reign forever."

    speech = "\n".join([introduction, leader_statement, repeated_message, rhetorical_question, core_values,
                        call_to_action, emotional_appeal, vision_for_future, closing])
    return speech

if __name__ == "__main__":
    config = load_config('config.json')
    speech = generate_speech(config)
    print(speech)
