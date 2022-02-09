# Goal: recompute versions on develop and master branch
# return {'include': [{'file': 'internal', 'version': 1.1.0, 'branch': 'master'}, {'file': 'external', 'version': 1.1.0, 'branch': 'develop'}, {'file': 'data_science', 'version': 1.1.0, 'branch': 'master'}]}

version_matrix = = {'include': []}

# Get latest_release_version
latest_release_version = ?

# Get new version on develop branch
# params:
#   latest_release_version
#   develop_version_in_file(file_name)
#   intent_list from .github/intent.yml from develop branch
#   do a loop to calculate new versions
# Append result behind and set branch as 'develop'

# Get new version on master branch
# params:
#   latest_release_version
#   master_version_in_file(file_name)
#   intent_list from .github/intent.yml from master branch
#   do a loop to calculate new versions
# Append result behind and set branch as 'master'

print(json.dumps(version_matrix))
