package main

import (
	"fmt"
	"math/rand"
	"time"
)

type DiscreteUniform struct {
	values[] int
}

func NewDiscreteUniform(values []int) *DiscreteUniform{
	v := make([]int, len(values))
	copy(v, values)
	return &DiscreteUniform{values: v}
}

func ( d *DiscreteUniform) Draw() int {
	return d.values[rand.Intn(len(d.values))]
}

func main() {
	rand.Seed(time.Now().UnixNano())
	diceValues := make([]int, 0, 6)
	for i := 1; i <= 6; i++{
		diceValues = append(diceValues, i)
	}

	Pdice := NewDiscreteUniform(diceValues)

	fmt.Println("P_dice = Uniform(1..6)")

	for i := 0; i < 2; i++ {
		fmt.Printf("%dth throw: %d\n", i+1, Pdice.Draw())
	}
}