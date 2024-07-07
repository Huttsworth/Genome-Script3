const vscode = require('vscode');
const assert = require('assert');

describe('Extension Test Suite', () => {
    beforeAll(() => {
        vscode.window.showInformationMessage('Start all tests.');
    });

    it('Sample test', () => {
        assert.strictEqual(-1, [1, 2, 3].indexOf(4));
    });
});
