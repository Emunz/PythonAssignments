class Call(object):
    id = 1
    def __init__(self, caller_name, phone_number, time, reason):
        self.id = Call.id
        Call.id += 1
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display_info(self):
        print "Unique ID:", self.id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", self.phone_number
        print "Time of Call:", self.time
        print "Reason for Call:", self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, caller_name, phone_number, time, reason):
        self.calls.append(Call(caller_name, phone_number, time, reason))
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def queue_info(self):
        for calls in self.calls:
            print "Name:", calls.caller_name
            print "Phone Number:", calls.phone_number
            print "ID:", calls.id
        print "Queue Length:", len(self.calls)
        return self

    def remove_number(self, number):
        for callers in self.calls:
            if callers.phone_number == number:
                self.calls.remove(callers)
        return self

    def print_time(self):
        for callers in self.calls:
            print callers.time
        

center = CallCenter()
center.add('Dan Emunds', '769-1451', '15:23', 'Troubleshooting')
center.add('Evan Munz', '341-0138', '15:44', 'Broken Equipment')
center.add('Steve Compere', '979-7920', '15:49', 'Dead')
center.add('Paul Leo', '986-2410', '16:01', 'Too Far')
# center.remove_number('341-0138')
# center.remove_number('979-7920')
# center.remove()
center.print_time()
center.queue_info()


# for calls in center.calls:
#     print calls.phone_number




