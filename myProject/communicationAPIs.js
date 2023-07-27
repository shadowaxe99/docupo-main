// communicationAPIs.js

const SlackAPI = require('./communicationAPIs/slack');
const MicrosoftTeamsAPI = require('./communicationAPIs/microsoftTeams');
const WhatsAppAPI = require('./communicationAPIs/whatsapp');
const TelegramAPI = require('./communicationAPIs/telegram');
const DiscordAPI = require('./communicationAPIs/discord');
const ZendeskAPI = require('./communicationAPIs/zendesk');
const TwilioAPI = require('./communicationAPIs/twilio');
const FacebookMessengerAPI = require('./communicationAPIs/facebookMessenger');

// Initialize API instances
const slack = new SlackAPI();
const microsoftTeams = new MicrosoftTeamsAPI();
const whatsapp = new WhatsAppAPI();
const telegram = new TelegramAPI();
const discord = new DiscordAPI();
const zendesk = new ZendeskAPI();
const twilio = new TwilioAPI();
const facebookMessenger = new FacebookMessengerAPI();

// Function to send message to Slack
function sendToSlack(message) {
  slack.sendMessage(message);
}

// Function to send message to Microsoft Teams
function sendToMicrosoftTeams(message) {
  microsoftTeams.sendMessage(message);
}

// Function to send message to WhatsApp
function sendToWhatsApp(message) {
  whatsapp.sendMessage(message);
}

// Function to send message to Telegram
function sendToTelegram(message) {
  telegram.sendMessage(message);
}

// Function to send message to Discord
function sendToDiscord(message) {
  discord.sendMessage(message);
}

// Function to send message to Zendesk
function sendToZendesk(message) {
  zendesk.sendMessage(message);
}

// Function to send message to Twilio
function sendToTwilio(message) {
  twilio.sendMessage(message);
}

// Function to send message to Facebook Messenger
function sendToFacebookMessenger(message) {
  facebookMessenger.sendMessage(message);
}

module.exports = {
  sendToSlack,
  sendToMicrosoftTeams,
  sendToWhatsApp,
  sendToTelegram,
  sendToDiscord,
  sendToZendesk,
  sendToTwilio,
  sendToFacebookMessenger
};