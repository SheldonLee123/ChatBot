CC=g++

INC_PATH = -I../../../include\
           -I../../../include/ASR\
           -I./include
# 程序名称
TARGET = asrDemo 
# cpp hpp源代码路径
SRC_PATH = ../src

# .o 临时目录
OBJ_PATH = obj

# 编译 libasrdemo.a
CFLAGS_LIB = $(INC_PATH) -fPIC -g  -O0 -Wall -Wno-unknown-pragmas  -D__LINUX__
LIB_SOURCE = $(wildcard $(SRC_PATH)/asrdemo_*.cpp)  
LIB_OBJECT = $(patsubst %.cpp,$(OBJ_PATH)/%.o,$(notdir $(LIB_SOURCE)))

# 编译 demo
CFLAGS_DEMO = $(INC_PATH) -fPIC  -g  -O0  -Wall -Wno-unknown-pragmas -Wno-unused-function -D__LINUX__ 
DEMO_SOURCE = $(wildcard $(SRC_PATH)/yours_*.cpp)
DEMO_OBJECT = $(patsubst %.cpp,$(OBJ_PATH)/%.o,$(notdir $(DEMO_SOURCE)))

# .a 库
LIBS = lib/libasrdemo.a ../../../lib/libBDSpeechSDK.a $(wildcard ../../../extern/lib/*.a)  
# Xlinker 参数
XFLAGS =  $(LIBS) -lrt -ldl -lpthread 

$(TARGET):init lib/libasrdemo.a $(DEMO_OBJECT)
	$(CC) $(DEMO_OBJECT) -o  $(TARGET)  -Xlinker "-("  $(XFLAGS) -Xlinker "-)"
	@echo
	@echo "Build Success"
	@echo "Type : ./$(TARGET)"

init:
	mkdir -p $(OBJ_PATH)
# lib 目录 libasrdemo.a
	mkdir -p lib 
#  头文件 目录
	mkdir -p include 
	cp $(SRC_PATH)/*.h*  include 

lib/libasrdemo.a:$(LIB_OBJECT) 
	ar cr lib/libasrdemo.a $(LIB_OBJECT) 


$(OBJ_PATH)/asrdemo_%.o:$(SRC_PATH)/asrdemo_%.cpp
	$(CC) $(CFLAGS_LIB) -c  $< -o $@
$(OBJ_PATH)/yours_%.o:$(SRC_PATH)/yours_%.cpp
	$(CC) $(CFLAGS_DEMO) -c  $< -o $@
clean:
	-rm -rf lib include $(OBJ_PATH) $(TARGET) BDS_Ident.dat asrdemo.log 
