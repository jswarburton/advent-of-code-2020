set -euo pipefail

if [ "$#" -ne 1 ]
then
  echo "One argument required"
  echo "Usage: ./setup_day.sh <DAY_NUMBER>"
  exit 1
fi

echo "Creating files for day $1"

padded_date=$(printf "%02d" $1)

touch src/main/python/day_"${padded_date}".py
touch src/test/python/day_"${padded_date}"_test.py

echo "Successfully created files"