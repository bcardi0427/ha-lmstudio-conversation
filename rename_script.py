import os

files_to_update = [
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_migrations.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_entity.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_conversation_agent.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_config_flow.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_basic.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\tests\lmstudio_conversation\test_ai_task.py",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\docs\Model Prompting.md",
    r"f:\AntiGravity Sources\HA-LLM-Interface\home-llm\docs\Backend Configuration.md",
]

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('llama_conversation', 'lmstudio_conversation')
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes needed: {file_path}")
    else:
        print(f"File not found: {file_path}")
