# Chatbot-Movieticketbooking-form 
Chatbots
# Create environment for Rasa in Anaconda prompt
conda create -n rasa python=3.6 anaconda
# Activate the rasa environment
conda activate rasa
# Go to folder where you want to create Bot
mkdir movieticketbooking_form
# Cretae the new Rasa project
rasa init
# Train the model
rasa train
# Run the bot
rasa shell
# Visualization
rasa interactive
# To test the bot with Rasa UI
rasa x
