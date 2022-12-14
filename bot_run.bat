@echo off

call %~dp0RGK_priceBot\venv\Scripts\activate

cd %~dp0RGK_priceBot
set TOKEN=5380382226:AAEMNfCek5xaljvTIjlyXHy5zUiBpGFirCI
python bot_teleg.py

pause