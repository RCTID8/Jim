set -e

git add .
echo "Please enter your commit message."
sleep 1
nano .commit_msg

echo "Adding commit message"
git commit -m "`cat .commit_msg`"

echo "Pushing...."
git push origin master
