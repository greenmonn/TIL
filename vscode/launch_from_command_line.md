# Launch VS Code from Command Line

PATH를 등록하면 code를 command line에서 바로 실행할 수 있다. (진작 안해놨던 것이 후회된다.)

```
cat << EOF >> ~/.bash_profile
# Add Visual Studio Code (code)
export PATH="\$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
EOF
```

https://code.visualstudio.com/docs/setup/mac 를 읽어보자.