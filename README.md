{
  "name": "whatsapp-bot",
  "description": "A simple WhatsApp bot built with Flask and Twilio",
  "repository": "https://github.com/x99-wong/Btoxis",
  "keywords": ["whatsapp", "twilio", "flask", "bot"],
  "env": {
    "TWILIO_ACCOUNT_SID": {
      "description": "Your Twilio Account SID",
      "required": true
    },
    "TWILIO_AUTH_TOKEN": {
      "description": "Your Twilio Auth Token",
      "required": true
    },
    "TWILIO_PHONE_NUMBER": {
      "description": "Twilio WhatsApp Number (e.g., whatsapp:+14155238886)",
      "required": true
    }
  },
  "buildpacks": [
    {
      "url": "heroku/python"
    }
  ]
}# WhatsApp Bot — Btoxis

![XXXTentacion Banner](https://upload.wikimedia.org/wikipedia/commons/9/9d/XXXTentacion_at_Rolling_Loud.jpg)

> **"People always leave. Don't get too attached."**  
> — XXXTentacion

---

### Made by: **Xxxwongtocion**
- From: **Tanzania**
- Passionate **bot developer**, focused on WhatsApp automations
- Open to collaborations & learning — *hit me up!*

---

## About This Bot

This is a simple WhatsApp bot built using **Python**, **Flask**, and **Twilio API**.  
It automatically replies to messages like `hi`, `bye`, and `help`.

---
---

{
  "name": "whatsapp-bot",
  "description": "A simple WhatsApp bot using Twilio and Flask",
  "repository": "https://github.com/x99-wong/Btoxis",
  "env": {
    "TWILIO_ACCOUNT_SID": {
      "description": "Your Twilio Account SID",
      "required": true
    },
    "TWILIO_AUTH_TOKEN": {
      "description": "Your Twilio Auth Token",
      "required": true
    },
    "TWILIO_PHONE_NUMBER": {
      "description": "Your Twilio WhatsApp number (e.g., whatsapp:+14155238886)",
      "required": true
    }
  },
  "dockerfile": "Dockerfile"
}
