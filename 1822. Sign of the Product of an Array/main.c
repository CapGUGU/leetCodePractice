int arraySign(int *nums, int numsSize)
{
    int NegNum = 0; // if negetive number is odd, then true, otherwise false
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] == 0)
            return 0;
        else if (nums[i] < 0)
            NegNum = NegNum + 1;
    }
    if (NegNum % 2 != 0)
        return -1;
    else
        return 1;
}