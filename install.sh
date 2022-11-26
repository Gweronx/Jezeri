echo "NOTE: This installer needs the Github CLI to be installed!"
cd ~
mkdir JZ
cd JZ
gh repo clone Gweronx/Jezeri
echo 'export PATH="$HOME/JZ/Jezeri:$PATH"' >> ~/.bashrc
echo 'alias jezeri="python3 jezeri.py $1"' >> ~/.bashrc
