# Script generated with Bloom
pkgdesc="ROS - <p> This package contains the robot model that is used by the realtime controllers inside <a href="http://www.ros.org/wiki/pr2_controller_manager">controller manager</a>. This robot model focuses on controlling the robot mechanism in a realtime control loop, and therefore it only contains the components of a robot that are relevant in realtime: the robot joints (with encoders, transmisisons and actuators) and the kinematic/dynamic model of the robot. </p> <p> The pr2_mechanism_model package is well tested and is released with a stable API. </p>"
url='http://ros.org/wiki/pr2_mechanism_model'

pkgname='ros-kinetic-pr2-mechanism-model'
pkgver='1.8.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-hardware-interface>=0.13.0'
'ros-kinetic-kdl-parser'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-hardware-interface'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-rosunit'
'ros-kinetic-urdf'
'urdfdom'
)

depends=('ros-kinetic-angles'
'ros-kinetic-hardware-interface'
'ros-kinetic-kdl-parser'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-hardware-interface'
'ros-kinetic-roscpp'
'ros-kinetic-urdf'
'urdfdom'
)

conflicts=()
replaces=()

_dir=pr2_mechanism_model
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_mechanism_model $srcdir/pr2_mechanism_model
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

