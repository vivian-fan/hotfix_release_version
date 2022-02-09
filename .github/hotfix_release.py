# Goal: recompute versions on develop and master branch
# return {'include': [{'file': 'internal', 'version': 1.1.0, 'branch': 'master'}, {'file': 'external', 'version': 1.1.0, 'branch': 'develop'}, {'file': 'data_science', 'version': 1.1.0, 'branch': 'master'}]}

version_matrix = {'include': []}

# Get latest_release_version
latest_release_version = ?

# Get new version on develop branch
# params:
#   latest_release_version
#   develop_version_in_file(file_name)
#   intent_list from .github/intent.yml from develop branch
#   do a loop to calculate new versions
# Append result behind and set branch as 'develop'

# intent_list from .github/intent.yml 
# {'external': ['major', 'minor'], 'external': ['minor', 'minor'], 'data_science': ['major']}
# return {'external': 'major', 'external': 'minor', 'data_science': 'major'}

intent_dic = {'external': 'major', 'external': 'minor', 'data_science': 'major'}
for file in intent_dic:
  file_name = file + '.yml'
  target_version = get_target_version(target_branch, file_name)
  new_version = calculate_version(intent_dic[file], target_version, latest_release_version)
  version_matrix['include'].append({'file': file_name, 'version': new_version, 'branch': target branch})

# Get new version on master branch
# params:
#   latest_release_version
#   master_version_in_file(file_name)
#   intent_list from .github/intent.yml from master branch
#   do a loop to calculate new versions
# Append result behind and set branch as 'master'

print(json.dumps(version_matrix))
