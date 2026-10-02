#!/usr/bin/env python3


class NewsSubject:
    def __init__(self):
        self._subs = {}

    def subscribe(self, observer, topics=None):
        if observer in self._subs:
            return
        self._subs[observer] = topics

    def unsubscribe(self, observer):
        self._subs.pop(observer, None)

    def notify(self, topic, data):
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()
    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
