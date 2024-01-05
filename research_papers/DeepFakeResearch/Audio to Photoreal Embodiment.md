# Audio to Photoreal Embodiment

> Conference: None
> Company: FAIR

## Introduction
1. Ques1: Interactions are robotics and uncanny; Sol1: Developing conversational avatars with level of photorealism that can capture indetail movements of the face and the body. The current approaches synthesis high frequency gestures of body movement. This is done using VqVae.
2. Ques2: No dataset to work with high realism due to lack of high frequnecy details. Sol2: Create an 8hr dataset of 2 persons with high quality infomation.
3. Ques3: Validity of evaluation for generation of high qual op. Sol3: Different metrics been proposed to generate the good op.
4. Ques4: No model generate all 3(face, body, hands) in realistic manner. Sol4: Present the combination of models to get things realsitic.

## Method
1. We have face diffusion model and body diffusion model.
2. The face diffusion model generates sequnce of facial expression codes the body diffusion model generate joint angles of the the body.
3. The input to the model is audio, for getting the embedding we are using wav2vec.
4. The output is a registered geometry for and view dependent texture using a CVAE.
5. Results are check on the 2d pic generated over 3d meshes to check the realism.


![images](https://drive.google.com/uc?export=view&id1B5QQLRLHFv-5WbtIWoFFzw9y-7KycN_G)
![images](https://drive.google.com/uc?export=view&id=1TIL1gx_O08IPd62qxJMasdbbku6D3QTH)
![images](https://drive.google.com/uc?export=view&id=1tjASN8Er-H_zYhQ0UTUflXyo0zrGkafQ)
![images](https://drive.google.com/uc?export=view&id=15Rw8HCRAbijMmEm8H74iE5x3qVfQL3wO)



## Metrics

> FD: Frechet Distance
1. FD(g): Geometric Realism measured by GT and Generated static poses.
2. FD(k): Kinematic motion realism, this distribution is calculated on the velocities of motion seq.
3. Div(g): Geometric pose diversity.
4. Div(k): Temporal variance across a seq of expression/poses. Measures amount of motion in a seq.
5. Div(samples): from the same audio, calculate the variance across samples.
6. Lipmotion: Vertical and horizontal distance, the vertical denotes the opening and closing, the horizontal denotes similing or other expressions.

## Limitations
1. Works on short audio clips. 
2. Limited to 4 people in the dataset for generation of output.

## To Understand

