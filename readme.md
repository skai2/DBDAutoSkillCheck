# Dead by Daylight: Auto Skill Check
<p align="center">
  <img src="assets/skillgif.gif" />
</p>

Auto skill check program will continuously monitor Dead by Daylight for active skill checks and attempt to hit great skill checks as accurately as possible. The program does not hack into the game in any manner, it is entirely external and relies on computer vision and image processing, attempting to simulate how a human interacts with the game.

The program was developed for educational purposes only (and because I deeply enjoy CV and DBD). Usage in real games may violate the game TOS and result in a ban, etc.

To any DBD and CV enthusiast devs out there, please feel free to experiment / raise issues / send in PRs / all that jazz, so together we can create the best possible auto skill check!

## Requirements:
* Windows Operating System
* 1080p widescreen or ultrawide resolution
* Default game skill check key binding (space)
* Default game UI settings

## Setup and Usage:
_Requires **python 3** and **git**_
1. Clone this repository and navigate to directory
```sh
git clone https://github.com/skai2/DBDAutoSkillCheck.git
cd DBDAutoSkillCheck

```
2. Setup python virtual environment and requirements
```sh
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

```
3. Run program
```sh
python skillcheck/skillcheck.py

```
OR If using multiple monitors:
```
python skillcheck/skillcheck.py --monitor [MONITOR_NUMBER]

```

## Development Status
Work in progress:
 * Improve great skill check accuracy
 * Impove general reliability

Planned roadmap:
 * Add configuration options
 * Add support for wiggle
 * Add support for madness
 * More to come...

## Very Useful Links:
* Skill Check [Simulator](https://dbd.lucaservers.com/) @ lucasservers.com
* Skill Check Process Ideas [p1](https://www.bottersgonnabot.com/automating-skill-checks-in-dead-by-daylight-part-i/) [p2](https://www.bottersgonnabot.com/automating-skill-checks-in-dead-by-daylight-part-ii/) @ bottersgonnabot
     
## WARNING:

Use at your own risk...

That's it lol.

# Email Contact

skai2mail@gmail.com
                                                               
