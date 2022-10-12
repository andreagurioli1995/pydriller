from repository import Repository


#url = "https://github.com/mozilla/addons-server"
url="https://github.com/pallets/flask"
for commit in  Repository(path_to_repo=url,only_modifications_with_file_types=".py", num_workers=1).traverse_commits():
    a= commit.modified_files
print("finished!")