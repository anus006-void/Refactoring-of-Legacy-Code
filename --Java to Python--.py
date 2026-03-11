class ComputeStatistics:

    def computeStats(self, file):
        total = 0
        sum = 0
        average = 0
        minimum = 0
        maximum = 0

        try:
            with open(file, "r") as br:
                line = br.readline()

                if not line:
                    return

                firstLine = int(line.strip())
                minimum = firstLine
                maximum = firstLine

                while line:
                    num = int(line.strip())
                    total += 1
                    sum += num

                    if minimum > num:
                        minimum = num

                    if maximum < num:
                        maximum = num

                    line = br.readline()

                print("total =", total)
                print("summation =", sum)
                print("average =", round(sum / total))
                print("Minimum =", minimum)
                print("Maximum =", maximum)

        except IOError as e:
            print(e)


def main():
    cs = ComputeStatistics()
    cs.computeStats("random_nums.txt")


if __name__ == "__main__":
    main()