if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TheBlackxyz/TheBlackKingBot.git /TheBlackKingBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TheBlackKingBot
fi
cd /LazyPrincess
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python bot.py
