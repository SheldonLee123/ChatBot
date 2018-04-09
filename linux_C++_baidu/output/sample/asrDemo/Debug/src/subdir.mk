################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/asrdemo_BdSpeechControl.cpp \
../src/asrdemo_ResultListener.cpp \
../src/asrdemo_Util.cpp \
../src/yours_PrintResultListener.cpp \
../src/yours_main.cpp 

OBJS += \
./src/asrdemo_BdSpeechControl.o \
./src/asrdemo_ResultListener.o \
./src/asrdemo_Util.o \
./src/yours_PrintResultListener.o \
./src/yours_main.o 

CPP_DEPS += \
./src/asrdemo_BdSpeechControl.d \
./src/asrdemo_ResultListener.d \
./src/asrdemo_Util.d \
./src/yours_PrintResultListener.d \
./src/yours_main.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -I"/home/fu/workspaceLinuxSDK/BDSpeechSDK/sample/asrDemo/src" -I../../../include/ASR -I../../../include -O0 -g3 -Wall -D__LINUX__  -c -fmessage-length=0  -Wno-unknown-pragmas -fPIC -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


