---
layout: post
title: "GNSS-Chapter 8 Parameter Estimation"
date:   2022-10-13 00:10:43 +0800
categories: gnss
---


# Chapter 8 Parameter Estimation

## Questions

`Why do we need to estimate parameters?`

`How to better estimate parameters?`

`Measurement Model for Least-squares Estimstion`

`Basic Least-squares Estimation`

`Recursive Least-squares Algorithm`

## TODO

**`Why do we need to estimate parameters?`**  

In GNSS positioning ,the parameters to be solved for can be coordinates, velocities, accelerations, attitudes/angles, or clock errors, depending the application.  

When we build the observation model with unknown parameters and have the observation, we need to use the above two to find the unknown parameters to get more accurate observation model.  


**`How to better estimate parameters?`**  

**Optimal estimation**  

*Optimal*  
Optimal estimatin plays a core role in solving unknown parameters from measurements. The criterion for an optimal estimation of the parameters can be different  

*the minimum L2 norm citerion*  

In most cases, the mininum L2 norm criterion is employed  

**the minimum L2 norm criterion**  
*Applicability*  
As long as the errors or noises of the measurements are Gaussianly distributed, the least-squares estimator is optimal in almost every conceivable sense. However, it is noted that Gaussian distribution is not strictly a prerequisite for this method to work in practice because even without the assumption of Gaussian distribution, the estimates are often still optimal among all linear estimators.

**`Measurement Model for Least-squares Estimstion`**

**`Basic Least-squares Estimation`**

**`Recursive Least-squares Algorithm`**




## Homework

`Please duduce the formula of basic least-squares and Recursive least-squares by oneself.`(递归最小二乘法)

`Please make program of Least Square Method on Computer and estimate parameters by using it.`



