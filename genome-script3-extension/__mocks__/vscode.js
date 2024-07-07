module.exports = {
  window: {
    showInformationMessage: jest.fn().mockResolvedValue('mocked showInformationMessage')
  },
  commands: {
    registerCommand: jest.fn()
  }
};
