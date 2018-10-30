import openpyxl

from statistic import Stat


class DataHandler:
    evaluator = Stat()

    @classmethod
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        return dic

    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.year_class = year_class

        self.cache = {}

    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())

        return self.cache.get('scores')

    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(
                self.get_scores()
            )

        return self.cache.get('average')

    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(
                self.get_scores(), self.get_average()
            )

        return self.cache.get('variance')

    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation'] = self.evaluator.std_dev(
                self.get_variance()
            )

        return self.cache.get('standard_deviation')


    def evaluate_class(self, total_avrg, sd):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()

        if avrg < total_avrg and std_dev > sd:
            print("성적이 너무 저조하고 학생들의 실력차이가 너무 크다")
        elif avrg > total_avrg and std_dev > sd:
            print("성적은 평균 이상이지만 학생들의 실력차이가 크다. 주의 요망")
        elif avrg < total_avrg and std_dev < sd:
            print("학생들의 실력차이는 크지 않지만 성적이 너무 저조하다. 주의 요망")
        elif avrg > total_avrg and std_dev < sd:
            print("성적도 평균이상이고 학생들의 실력차이도 크지 않다.")

    def get_evaluation(self, total_avrg, sd = 20):
        print('*' * 50)
        print('{} 반 성적 분석 결과'.format(self.year_class))
        print(
            "{0}반의 평균은 {1}점이고 분산은 {2}이며 따라서 표준편차는 {3}이다".format(
                self.year_class,
                self.get_average(),
                self.get_variance(),
                self.get_standard_deviation()
            )
        )
        print('*' * 50)
        print('{} 종합평가'.format(self.year_class))
        print('*' * 50)
        self.evaluate_class(total_avrg, 50)