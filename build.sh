echo "DetectSyS installer v0.0.0 "
echo "Installing prerequisites "
echo "Installing dependencies "

chmod +x scan.py
sudo cp -r scan.py /usr/bin/
if [ $? -eq 0 ]; then
    echo [SUCCESS] Copied binary to /usr/bin 
else
    echo [ERROR] Unable to copy
    ecit 1
fi

