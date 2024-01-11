# Python for Experimental Research and Analysis Workshop

![00539-147397801-experimental research and analysis, empty room, cyberpunk, dark psychedelic colors, futuristic, cognition, science](https://github.com/zeyus/PyResearchWorkshop/assets/75656/f94cbca9-db0d-4960-9ade-8a27d0affe76)

## Preparation

Most of what we will work with will be provided in this GitHub repository, but there are a few things you can get set up so we don't have to spend time on it during the workshop.

### Tools

Please have the following tools installed on your computer:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#miniforge3) *Note: please remember the location where miniforge is installed, e.g. `C:\Users\myusername\miniforge3` or `/home/myusername/miniforge3`.*
- [VScode](https://code.visualstudio.com/)

### Environment Setup

Now that you have the tools installed, you can try setting up an [environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) that we will work with. Give it a go, if you get stuck, no problems, we can finish setting up at the start of the workshop. Please follow the appropriate instructions for your computer and operating system.

#### Windows PC

1. Open a terminal with `⊞ + R` (Windows key + R) and type `cmd.exe` and press enter
2. You should see a window like the following:<br/><img width="352" alt="image" src="https://github.com/zeyus/PyResearchWorkshop/assets/75656/cab5effe-2f45-4e77-b02f-ea2d6fa8516b">
3. Now we can make miniforge/conda commands available by running the command `C:\Users\myusername\miniforge3\condabin\mamba.bat init --all` *remember to replace "myusername" with your username, the path should match the miniforge install location*. You will see a list of different [shells](https://en.wikipedia.org/wiki/Shell_(computing)) which miniforge will try to set up, you will probably only see a couple that say `modified`, this is normal
5. Close the terminal
6. Open a terminal again (the same way as step 1)
7. Paste the following command in the terminal `mamba create -y -c conda-forge -c cogsci -npyworkshop python=3.10 psychopy pygame ipykernel matplotlib scipy scikit-learn numpy seaborn pandas` and press enter.
8. You'll see an install progress and then text that looks something like:<br/>![image](https://github.com/zeyus/PyResearchWorkshop/assets/75656/c60510df-8a4b-4016-aced-82a1351e1582)

Congrats, it's all ready to go!

#### Mac OSX / Linux

1. Open a terminal with `CMD + space` and search for "Terminal", or open a terminal from Applications
2. You should see a terminal window open
3. Now we can make miniforge/conda commands available by running the command `/home/myusername/miniforge3/condabin/mamba init --all` *remember to replace "myusername" with your username, the path should match the miniforge install location*. You will see a list of different [shells](https://en.wikipedia.org/wiki/Shell_(computing)) which miniforge will try to set up, you will probably only see a couple that say `modified`, this is normal
5. Close the terminal
6. Open a terminal again (the same way as step 1)
7. Paste the following command in the terminal `mamba create -y -c conda-forge -c cogsci -npyworkshop python=3.10 psychopy pygame ipykernel matplotlib scipy scikit-learn numpy seaborn pandas` and press enter.
8. You'll see an install progress and then text that looks something like:<br/>![image](https://github.com/zeyus/PyResearchWorkshop/assets/75656/c60510df-8a4b-4016-aced-82a1351e1582)

Congrats, it's all ready to go!

## Workshop

... more to come
