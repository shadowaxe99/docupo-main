from flask import Flask, request, jsonify
from backend.document_parser import parseDocument
from backend.repository_generator import generateRepoStructure
from backend.github_integration import createGithubRepo, pushToGithub
from backend.notification_system import notifyUser

app = Flask(__name__)

DOCUMENT_FORMATS = ['pdf', 'docx', 'txt']
GITHUB_API_KEY = 'your_github_api_key'

@app.route('/upload', methods=['POST'])
def uploadDocument():
    file = request.files['document']
    if file and file.filename.rsplit('.', 1)[1].lower() in DOCUMENT_FORMATS:
        try:
            document_data = parseDocument(file)
            repo_structure = generateRepoStructure(document_data)
        except Exception as e:
            return jsonify({'message': 'Error processing document: ' + str(e)}), 500
        return jsonify(repo_structure), 200
    else:
        return jsonify({'message': 'Invalid file format'}), 400

@app.route('/review', methods=['POST'])
def reviewRepoStructure():
    repo_structure = request.json.get('repo_structure')
    if repo_structure:
        try:
            repo_url = createGithubRepo(GITHUB_API_KEY, repo_structure)
            pushToGithub(GITHUB_API_KEY, repo_url, repo_structure)
            notifyUser('REPO_SUCCESS')
        except Exception as e:
            return jsonify({'message': 'Error creating repository: ' + str(e)}), 500
        return jsonify({'message': 'Repository created successfully'}), 200
    else:
        return jsonify({'message': 'Invalid repository structure'}), 400

if __name__ == '__main__':
    app.run(debug=True)