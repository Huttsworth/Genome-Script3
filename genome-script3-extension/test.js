const vscode = require('vscode');
const extension = require('./out/extension');

// Mock the vscode window.showInformationMessage method
vscode.window.showInformationMessage = jest.fn();

// Mock the vscode.commands.registerCommand method
vscode.commands.registerCommand = jest.fn((command, callback) => {
    return { _command: command, _callback: callback };
});

describe('Extension Test Suite', () => {
    it('should register the helloWorld command', () => {
        // Mock the context object with subscriptions
        const context = { subscriptions: [] };

        // Call the activate function with the mock context
        extension.activate(context);

        // Check if the command has been registered
        expect(vscode.commands.registerCommand).toHaveBeenCalledWith('genome-script3-extension.helloWorld', expect.any(Function));

        // Simulate running the 'helloWorld' command
        const helloWorldCommand = context.subscriptions.find(sub => sub._command === 'genome-script3-extension.helloWorld');

        if (helloWorldCommand) {
            helloWorldCommand._callback();
        }

        // Check if the showInformationMessage method was called
        expect(vscode.window.showInformationMessage).toHaveBeenCalledWith('Hello World from genome-script3-extension!');
    });
});
