const GPT3_5 = require('gpt3.5');

class Gpt3_5 {
  constructor() {
    this.model = new GPT3_5();
  }

  async draftEmailResponse(emailContent) {
    try {
      const response = await this.model.generateResponse(emailContent);
      return response;
    } catch (error) {
      console.error('Error in drafting email response:', error);
      throw error;
    }
  }

  async sendFollowUp(email) {
    try {
      const response = await this.model.generateFollowUp(email);
      return response;
    } catch (error) {
      console.error('Error in sending follow-up:', error);
      throw error;
    }
  }
}

module.exports = Gpt3_5;