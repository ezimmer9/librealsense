/*
 * timer.h
 *
 *  Created on: May 8, 2018
 *      Author: ezimme9
 */

#ifndef EXAMPLES_CAPTURE_TIMER_H_
#define EXAMPLES_CAPTURE_TIMER_H_


#include <string.h>
#include <stdint.h>
#include <chrono>
#include <fstream>
#include <stdio.h>

using tp = std::chrono::system_clock::time_point;


#define WAIT_FOR_FRAME 1
#define DEPTH 2
#define RGB   3

enum timer_type{
	strat,
	end
};

struct timer_event{
	uint32_t event_ID;
	uint64_t time;
	timer_type type;
};

class timer {
private:
	uint32_t counter;
	std::mutex mtx;
    FILE *file;
    timer_event *buffer;

public:
	timer()
	{
		file = nullptr;
		counter=0;
		buffer = new timer_event[10000];
	}
	//~timer();

	uint64_t tp_to_long(std::chrono::system_clock::time_point tp)
	{
		return std::chrono::duration_cast<std::chrono::microseconds>(tp.time_since_epoch()).count();
	}

	std::chrono::system_clock::time_point now()
	{
		return std::chrono::system_clock::now();
	}
	void start_timer(uint32_t ID)
	{
		std::lock_guard<std::mutex> lock(mtx);
		buffer[counter] = {ID , tp_to_long(now()) , timer_type::strat};
		counter++;
	}
	void end_timer(uint32_t ID)
	{
		std::lock_guard<std::mutex> lock(mtx);
		buffer[counter] = {ID , tp_to_long(now()) , timer_type::end};
		counter++;
	}
	void save_events()
	{
		file = fopen("timer.txt" , "w");
	    for (int i=0 ; i < counter ; ++i){
	    	fprintf(file , "%u,%lu,%u\n" ,  buffer[i].event_ID , buffer[i].time ,  buffer[i].type );
	    }
	    fclose(file);
	}

};

std::shared_ptr<timer> timers;
void init_timer()
{
#ifndef TIMER
	timers = std::make_shared<timer>();
#endif
	return;
}

void START_TIMER(uint32_t id)
{
#ifndef TIMER
	timers->start_timer(id);
#endif
	return;
}

void END_TIMER(uint32_t id)
{
#ifndef TIMER
	timers->end_timer(id);
#endif
	return;
}

void save_timers()
{
#ifndef TIMER
	timers->save_events();
#endif
	return;
}

#endif /* EXAMPLES_CAPTURE_TIMER_H_ */
