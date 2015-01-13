Name:           ros-indigo-pr2-mechanism-model
Version:        1.8.16
Release:        0%{?dist}
Summary:        ROS pr2_mechanism_model package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_mechanism_model
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-angles
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-pr2-hardware-interface
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-urdf
Requires:       urdfdom-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-pr2-hardware-interface
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rosunit
BuildRequires:  ros-indigo-urdf
BuildRequires:  urdfdom-devel

%description
This package contains the robot model that is used by the realtime controllers
inside controller manager. This robot model focuses on controlling the robot
mechanism in a realtime control loop, and therefore it only contains the
components of a robot that are relevant in realtime: the robot joints (with
encoders, transmisisons and actuators) and the kinematic/dynamic model of the
robot. The pr2_mechanism_model package is well tested and is released with a
stable API.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 13 2015 Devon Ash <dash@clearpathrobotics.com> - 1.8.16-0
- Autogenerated by Bloom

