#!/bin/bash

if [ -d "allure-report/history" ]; then
  echo "🔁 Copying history to new allure-results..."
  mkdir -p allure-results/history
  cp -R allure-report/history/* allure-results/history/
else
  echo "ℹ️ No previous history found. This may be your first run."
fi

echo "📁 Collecting Allure results..."
pytest --alluredir=allure-results

echo "🛠️ Generating new Allure report..."
allure generate allure-results -o allure-report --clean

echo "🌐 Opening Allure report..."
allure open allure-report
