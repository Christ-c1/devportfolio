from flask import Flask, jsonify, request

app = Flask(__name__)

# Simuler une base avec une liste
profiles = []
profile_id_counter = 1


@app.route('/profiles', methods=['GET'])
def get_profiles():
    return jsonify(profiles)


@app.route('/profiles', methods=['POST'])
def create_profile():
    global profile_id_counter
    data = request.json
    data['id'] = profile_id_counter
    profiles.append(data)
    profile_id_counter += 1
    return jsonify(data), 201


@app.route('/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    for profile in profiles:
        if profile['id'] == profile_id:
            return jsonify(profile)
    return jsonify({'error': 'Profil non trouvé'}), 404


@app.route('/profiles/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    for profile in profiles:
        if profile['id'] == profile_id:
            profiles.remove(profile)
            return jsonify({'message': 'Profil supprimé'})
    return jsonify({'error': 'Profil non trouvé'}), 404


@app.route('/profiles/skills', methods=['GET'])
def get_profiles_by_skill():
    skill = request.args.get('skill')
    if not skill:
        return jsonify({'error': 'Paramètre "skill" manquant'}), 400
    filtered = [p for p in profiles if skill in p.get('skills', [])]
    return jsonify(filtered)


# Pour exécuter en local (optionnel)
if __name__ == '__main__':
    app.run(debug=True)
