# Deploying the AI Travel Planner on Streamlit Cloud

Follow these steps to deploy the AI Travel Planner on Streamlit Cloud:

## 1. Create a GitHub Repository

1. Create a new GitHub repository
2. Upload all project files to the repository:
   - app.py
   - utils.py
   - requirements.txt
   - .gitignore (include .env in this file)
   - README.md
   - sample_inputs.py (optional)
   - documentation.md (optional)

## 2. Set Up Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and main file path (app.py)
5. Advanced settings:
   - Set the Python version to 3.9 or higher
   - Add the following secrets:
     ```
     OPENAI_API_KEY = your_openai_api_key
     SERPER_API_KEY = your_serper_api_key
     ```

## 3. Deploy Your App

1. Click "Deploy"
2. Wait for the build and deployment process to complete
3. Your app will be available at: https://[your-username]-ai-travel-planner.streamlit.app

## 4. Testing

After deployment, test the application with various inputs:
1. Complete travel information
2. Partial travel information that requires follow-up questions
3. Vague preferences that need refinement

## 5. Sharing Your Application

- Share the URL of your deployed application
- Include setup instructions for API keys if users need to deploy their own instance

## 6. Troubleshooting

If you encounter issues:
1. Check the Streamlit Cloud logs for error messages
2. Verify that your API keys are correctly set in the Streamlit secrets
3. Ensure all dependencies are properly listed in requirements.txt
4. Check that your .gitignore file is not excluding essential code files 