# PBDT
Python Backdoor Detection Model Based on Combined Features

## Research paper

We present the findings of this work in the following research paper:

Fang Y, Xie M, Huang C. PBDT: Python Backdoor Detection Model Based on Combined Features[J]. Security and Communication Networks, 2021, 2021. [view](https://www.hindawi.com/journals/scn/2021/9923234/)

## Introduction

Application security is essential in today’s highly development period. Backdoor is a means by which attackers can invade the system to achieve illegal purposes and damage users’ rights. It has posed a serious threat to network security. Thus, it is urgent to take adequate measures to defense such attacks. Previous research work mainly focused on numerous PHP webshells, with less research on Python backdoor files. Language differences make the method not entirely applicable. This paper proposes a Python backdoor detection model named PBDT based on combined features. The model summarizes the common functional modules and functions in the backdoor files, and extracts the number of calls in the text to form sample features. What’s more, we consider the text’s statistical characteristics, including the information entropy, the longest string, etc., to identify the obfuscated Python code. Besides, the opcode sequence is used to represent code characteristics, such as TF-IDF vector and FastText classifier, to eliminate the influence of interference items. Finally, we introduce the random forest algorithm to build classifier. Covering most types of backdoors and some samples are obfuscated, the model achieves an accuracy of 97.70%, and the TNR index is as high as 98.66%, showing a good classification performance in Python backdoor detection.

## Backdoor data

The backdoor samples are mainly divided into three categories:

-  **github：**First of all, we collected a wide range of Github projects, including webshells, reverse shells, C/S backdoors written in Python language, and so on. The collected files were marked in the project introduction and verified by manual inspection to be malicious.
-  **msf：**Another part of the samples are generated using Metasploit Framework (MSF), an open-source security vulnerability detection tool with functions including the whole penetration testing process. The msfvenom module can generate Trojan programs. We have obtained part of the rebound shell through this tool, including some samples encoded by base64 or containing shellcode.
-  **veil：**In actual applications, backdoors are mostly obfuscated. In order to obtain more comprehensive data, we use the Veil-Evasion anti-virus tool, which can be used to generate Metasploit payloads and bypass standard software detection or killing. Combining these two tools, a high-quality sample that can bypass security controls is obtained.

## Reference

If you use the dataset in a scientific publication, we would appreciate citations using this Bibtex entry:

```
@article{fang2021pbdt,
  title={PBDT: Python Backdoor Detection Model Based on Combined Features},
  author={Fang, Yong and Xie, Mingyu and Huang, Cheng},
  journal={Security and Communication Networks},
  volume={2021},
  year={2021},
  publisher={Hindawi}
}
```

