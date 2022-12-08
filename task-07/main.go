package main

import (
	"strconv"
	"syscall/js"
)

var document js.Value

func inc(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	p := document.Call("getElementById", args[0])
	var value = p.Get("innerHTML").String()
	int1, _ := strconv.Atoi(value)
	p.Set("innerHTML", int1+1)
	return value
}

func dec(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	p := document.Call("getElementById", args[0])
	var value = p.Get("innerHTML").String()
	int1, _ := strconv.Atoi(value)
	p.Set("innerHTML", int1-1)
	return value
}

func reset(this js.Value, args []js.Value) interface{} {
	document := js.Global().Get("document")
	p := document.Call("getElementById", args[0])
	p.Set("innerHTML", 0)
	return nil
}

func registerCallbacks() {
	js.Global().Set("inc", js.FuncOf(inc))
	js.Global().Set("dec", js.FuncOf(dec))
	js.Global().Set("reset", js.FuncOf(reset))
}

func main() {
	c := make(chan struct{}, 0)
	println("Hello World")
	registerCallbacks()

	<-c
}
