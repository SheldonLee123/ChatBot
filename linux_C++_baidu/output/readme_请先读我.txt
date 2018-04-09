Linux C++ SDK 仅有在线长语音功能。

仅支持x64 linux 操作系统，　在centos 4 6 7 及ubuntu 14.04，　g++ 4.8 版本测试通过

SDK内部限制１０个线程并发，即最多支持１０个音频的实时识别。 

sample目录下有两个实例工程

sample/asr 运行 sh build_and_run.sh
sample/asrDemo 下 run目录中运行 sh build_and_run.sh 。同时也是为eclipseCDT工程， sample/asrDemo/run是运行目录。

