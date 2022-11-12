#!bash

# Rewrite all files into a.md
echo -e "---\ntitle: all\n---\n" > a.md

# README 部分
cat README.md>>a.md

# 自然地理学部分
cat chapter-1.md>>a.md
cat chapter-2.md>>a.md
cat chapter-3.md>>a.md
cat chapter-4.md>>a.md
cat chapter-5.md>>a.md
cat chapter-6.md>>a.md
#cat chapter-7.md>>a.md
cat guideline-ans.md>>a.md

# 人文地理学部分
cat chapter-8.md>>a.md
cat chapter-9.md>>a.md
cat chapter-10.md>>a.md
cat chapter-11.md>>a.md
cat guideline2-ans.md>>a.md

