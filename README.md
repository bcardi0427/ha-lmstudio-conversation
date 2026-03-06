# LM Studio Integration for Home Assistant

Connect your fully local Large Language Models running in **[LM Studio](https://lmstudio.ai/)** natively with your Home Assistant smart home!

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://my.home-assistant.io/redirect/hacs_repository/?category=Integration&repository=ha-lmstudio-conversation&owner=bcardi0427)

## 🌟 What is this?

This is a custom component designed specifically for interfacing with LM Studio's local OpenAI-compatible server. It provides a seamless, privacy-first, and completely local way to add AI chat and voice control to your smart home without relying on the cloud.

### ✨ Features
- **Plug-and-play LM Studio Support**: Specially configured to work flawlessly with LM Studio's endpoint.
- **Dynamic Model Fetching**: Automatically detects loaded models from your LM Studio instance during setup!
- **Voice & Chat Ready**: Integrate into the built-in Home Assistant conversation interfaces.
- **AI Automations**: Leverage local AI to make intelligent decisions in your smart home.
- **100% Local & Private**: No data leaves your local network.

---

## 🤝 Credits & Acknowledgements

This project is a fork of the amazing **[Home LLM](https://github.com/acon96/home-llm)** integration created by **Alex O'Connell (@acon96)**. 

The core engine of this integration relies heavily on the generic OpenAI API client developed by Alex. We have tailored it specifically for the LM Studio experience, separating it into its own Home Assistant domain (`lmstudio_conversation`) so users can install it cleanly alongside other setups. Please check out the original repository to support their incredible work!

---

## 🚀 Quick Setup Guide

### 1. Configure LM Studio
1. Open LM Studio.
2. Load a model (we highly recommend `openai/gpt-oss-20b` or smaller instruction-tuned models for speed).
3. Start the **Local Server** (typically running on `http://127.0.0.1:1234/v1`).
4. Ensure your server is accessible over your local network by enabling **CORS** and binding to `0.0.0.0` or your machine's IP address.

### 2. Install Integration in Home Assistant
You can install this via HACS (Home Assistant Community Store):
1. Go to HACS -> Integrations.
2. Click the 3 dots in the top right, select **Custom repositories**.
3. Add `https://github.com/bcardi0427/ha-lmstudio-conversation` with the category set to **Integration**.
4. Click Download and then **Restart Home Assistant**.

### 3. Add to Home Assistant
1. Go to **Settings** -> **Devices & Services**.
2. Click **Add Integration** and search for **LM Studio Integration**.
3. Enter your LM Studio server's IP address and Port (Defaults to `1234`).
4. The integration will automatically fetch the loaded model from LM Studio!

---

## 📝 Usage

Once installed, you can set the LM Studio Integration as your default **Conversation Agent** in Home Assistant's Voice Assistant settings. 

You can also use it in automations using the `conversation.process` service!

## 📜 License

This project is licensed under the MIT License - see the [LICENSES.txt](LICENSES.txt) file for details.
