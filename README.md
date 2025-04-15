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
}
