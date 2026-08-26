marco() {
    export MARCO_DIR=$(pwd)
    echo "Saved directory: $MARCO_DIR"
}
polo() {
    if [ -n "$MARCO_DIR" ]; then
        cd "$MARCO_DIR"
        echo "Switched to $MARCO_DIR"
    else
        echo "No directory saved. Run marco first."
    fi
}
