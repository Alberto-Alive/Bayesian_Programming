#include <iostream>
#include <random>
#include <vector>

class DiscreteUniform {
    public: explicit DiscreteUniform(std::vector<int> values)
    : values_(std::move(values)),
    rng_(std::random_device{}()),
    dist_(0, static_cast<int>(values_.size()) - 1) {}

    int draw() {
        return values_[dist_(rng_)];
    }

private:
    std::vector<int> values_;
    std::mt19937 rng_;
    std::uniform_int_distribution<int> dist_;
};

int main() {
    std::vector<int> dice_values;
    for (int i = 1; i <= 6; ++i) dice_values.push_back(i);

    DiscreteUniform P_dice(dice_values);
    std::cout << "P_dice = Uniform(1..6)\n";
    for (int i=0; i<2; ++i) {
        std::cout << (i+1) << "th throw: " << P_dice.draw() << "\n";
    }
    return 0;
}