Overview of the slides:
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/d56a7b4a-16d0-4b67-8059-12cd8bf3ae34)


## Recon of Humans
Dataset of EgoBody dataset:
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/2114fe61-da79-4b0a-b3a1-d272d4a0630f)
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/1ddfcc5a-2193-4bd8-8855-5b6e6975d581)



Recon the pose, motion from the cameras, motion blur is a major problem from ego centric POV. The distance between the people is small.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/6fe6d64e-1223-4f6f-9318-c297cac36cf6)

Image truncation, since the people are close to each other in the ego view.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/6a05de11-e30c-4093-8d55-9066deda785f)

from the 3d scene of the room, you can decide if the person is sitting or standing.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/96732e56-c624-4b62-9335-732ba9e856cd)


![image](https://github.com/saisriteja/IITMResearch/assets/48018142/97e7eeed-6e62-4f1b-9441-73e491a7e936)


There are deterministic and probabilistic models for generation of the human meshes.
We don't want the deterministic approach because there is no one particular solution for the given occluded part.
Probabilistic methods can help us during making a motion.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/833196b9-be70-41df-a307-b0907257f2e4)

EgoHMR
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/a06afb80-e6dd-4b4f-bf60-41f86e0d67f6)

Probabilistic Model to Generate Motion of the synthetic human
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/5545ee4c-0a2a-4e06-89f9-7ecc29f1b3e6)


The scene condition and image condition are feature vectors and they are given to the diffusion models.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/58890166-3ecd-4c98-9c1e-704e9c07c5bd)


Collision guidance is an important module to generate a proper mesh.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/f28967bd-b671-4117-944f-45dd758cb1ac)

Collision loss metric for proper modeling.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/d7e60189-8f49-4b8a-a347-8f4d31736713)

Further studies
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/105f68f2-27fc-4cf2-820e-bf3acaa65a72)

Motion priors are necessary when the person is not there in the egocentric but still needs to do the motion detection.

## Synthesis of Virtual Humans

1. Computer Graphics
2. Autonomous agents
3. Character Animations
4. Metaverse

Computer vision: Predict the next 2 seconds, given the first 2 seconds, the goal is accuracy and generalization.
Computer Graphics: Focus on motion realism and controllability.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/d242b733-1ede-4249-b2b2-82293738e1ad)

Diverse set of movements for the same task of walking.
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/656ac75d-a365-4862-8032-831461dbfce4)

![image](https://github.com/saisriteja/IITMResearch/assets/48018142/3c92bf44-ba1d-46b8-a7d0-ce74a522d168)
![image](https://github.com/saisriteja/IITMResearch/assets/48018142/f717e538-7bad-41d9-8ba4-449b3e3a5cd0)


![image](https://github.com/saisriteja/IITMResearch/assets/48018142/9fc12002-3af6-40aa-932d-d747f0b175c3)


Further discussion:

Long-term planning and social Interaction.
Leveraging 2d videos over 3d data.
