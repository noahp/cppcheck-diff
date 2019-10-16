int main(int argc, char **argv) {
    volatile int yolo[4];
    yolo[4] = 123;  // whoopsie!
    return 0;
}
