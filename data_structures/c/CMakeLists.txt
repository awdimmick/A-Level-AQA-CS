cmake_minimum_required(VERSION 3.20)
project(c C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(c
        graphs.c
        linked_list.c
        linked_list.h
        main.c
        queues.c
        queues.h
        stack.c
        stack.h graphs.h)
