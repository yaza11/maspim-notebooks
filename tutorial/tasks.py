DISABLE_QUIZZES: bool = True


class Task:
    answer = None

    def __init__(self,
                 solution: str | list[str],
                 options: list[str] | None = None,
                 explanation: str | None = None
    ) -> None:
        if not hasattr(solution, '__iter__'):
            solution = [solution]
        self._solution: list[str] = solution
        self._options: list[str] = options
        self._explanation: str | None = explanation

    def ask(self):
        if DISABLE_QUIZZES:
            return 
        self.answer: str = input('Enter your answer: ').strip()
        self._check_answer()

    def options(self):
        shuffled = [f'({i + 1}) {o}' for i, o in enumerate(self._options)]
        print('The following options are available '
              '(you can enter the number of the answer):')
        print('\n'.join(shuffled))

    def _check_answer(self):
        if len(self.answer) > 0 and (self.answer in self._solution):
            print('Correct!')
            if self._explanation is not None:
                print(self._explanation)
        else:
            print("Incorrect! But that's okay, you can try again")
            if self._options is not None:
                print(f"possible options are: '{"', '".join(self._options)}'")


##############################################################################
##############################################################################
##############################################################################
########## NOTHING OF INTEREST BELOW HERE ####################################
##############################################################################
##############################################################################
##############################################################################









































































##############################################################################
##############################################################################
##############################################################################
########## SERIOUSLY, STOP SCROLLING #########################################
##############################################################################
##############################################################################
##############################################################################





























































































# okay, here you go
chapter0_task1 = Task('3')
chapter0_task2 = Task(['True', 'true'], ['True', 'False'])

chapter1_task1 = Task('noisy', ['noisy', 'clean'])
chapter1_task2 = Task('yes', ['no', 'yes'])
chapter1_task3 = Task('C37:2')

chapter2_task1 = Task(['self._noise_level_subtracted',
                       '_noise_level_subtracted',
                       'noise_level_subtracted'])
chapter2_task2 = Task(
    ['10%', '10 %', '10'],
    ['14', '10', '0']
)

chapter3_task1 = Task('dark', ['light', 'dark'])
chapter3_task2 = Task(['3', 'a hat with ears', '(3)'],
                      ['a bunny face', 'a sunset', 'a hat with ears'])
chapter3_task3 = Task(
    ['2', '(2)'],
    ['To make the decision for the descriptor less difficult',
     'To avoid areas at the sample boundary',
     'To save memory'],
    'Areas at the boundary have a high contrast and result in angles '
    'roughly perpendicular to the lamination. Since we can be sure that the '
    'tilt angle of laminae is below 22.5 degrees, it is best to exclude angles '
    'with large angles'
)

chapter4_task1 = Task('yes',
                      ['yes', 'no'],
                      'only slightly but enough to cause issues if not addressed')
chapter4_task2 = Task(['1', '(1)'],
                      ['<1 degree', '>= 1 but <5', '>5 but < 10', '>10'])

chapter5_task1 = Task(
    '2',
    ["It is everywhere, so it doesn't tell us anything",
     'It has high abundances in holes',
     'It is noisy'],
    'In holes the signal of Si is very strong because the sample '
    'holder is made of glass. If the sample thins out, we could get a mixed '
    'signal of the glass and sample.'
)
chapter5_task2 = Task(
    ['2', '3'],
    [
        ('The punch hole identification is more difficult in this image because '
         'the holes are closer to the boundary of the image'),
        ('The punch hole detection is easier because the holes are more square '
         'shaped'),
        ('The algorithm does not care about hard and easy, it simply picks the '
         'pixels with the highest scores')
    ]
)

chapter6_task1 = Task(
    ['2', '3'],
    [
        'Get more handleable values',
        'Remove variations merely caused by higher sediment input',
        'Remove variations caused by variances in the matrix',
        'This is necessary if you want to calculate contrasts',
        'This keeps the values at a reasonable scale and prevents floating point precision losses'
    ]
)

chapter6_task2 = Task(
    ['1', '4'],
    [
        'They are correlated',
        'They are anti-correlated',
        'They are not correlated',
        'In some sections they are correlated, in others not'
    ]
)

