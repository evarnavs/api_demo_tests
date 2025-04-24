#!/bin/bash

echo "📁 Running tests and collecting Allure results..."
pytest --alluredir=allure-results

# Step 2: Copy previous history if it exists
if [ -d "allure-report/history" ]; then
  echo "🔁 Copying history to preserve trend..."
  cp -R allure-report/history allure-results/history
else
  echo "ℹ️ No previous history found. This may be your first run."
fi

# Step 3: Generate new Allure report
echo "🛠️ Generating new Allure report..."
allure generate allure-results -o allure-report --clean

# Step 4: Open in browser
echo "🌐 Opening Allure report..."
allure open allure-report
