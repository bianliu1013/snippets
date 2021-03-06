#include <boost/python.hpp>
#include "classes.h"

class HelloWrapper : public Hello, public boost::python::wrapper<Hello>
{
    public:
        void message() {
            // WARNING: here, message() doesn't return anything, so the wrapper neither.
            //          If message() had returned something, we would have written:
            //          "return this->get_override("message")();"
            this->get_override("message")();
        }
};

BOOST_PYTHON_MODULE(cppclasses)
{
    boost::python::class_<HelloWrapper, boost::noncopyable> hello_wrapper("Hello");
    hello_wrapper.def("message", boost::python::pure_virtual(&Hello::message), "Print a message.");
    hello_wrapper.def("get_name", &Hello::getName, "Get name.");
}
